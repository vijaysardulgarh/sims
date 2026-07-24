import React, { useState, useEffect } from 'react';
import { SubjectConstraintService } from "../services/subjectConstraintService";

const SubjectConstraintListPage = () => {
    const [classes, setClasses] = useState([]);
    const [streams, setStreams] = useState([]);
    const [subjectsMap, setSubjectsMap] = useState({}); // Lookup map for subject IDs to names
    
    const [selectedClass, setSelectedClass] = useState('');
    const [selectedStream, setSelectedStream] = useState('');
    
    // Holds requirements data mapped to form states
    const [requirements, setRequirements] = useState([]);
    const [formState, setFormState] = useState({});
    
    const [isSaving, setIsSaving] = useState(false);
    const [statusMessage, setStatusMessage] = useState({ type: '', text: '' });
    const [isLoadingData, setIsLoadingData] = useState(true);

    useEffect(() => {
        setIsLoadingData(true);
        Promise.all([
            SubjectConstraintService.getClasses(),
            SubjectConstraintService.getStreams(),
            SubjectConstraintService.getSubjects ? SubjectConstraintService.getSubjects() : Promise.resolve({ data: [] })
        ]).then(([classRes, streamRes, subjectRes]) => {
            setClasses(classRes.data?.results || classRes.data || []);
            setStreams(streamRes.data?.results || streamRes.data || []);
            
            // Build a fast lookup dictionary: { subjectId: subjectName }
            const subs = subjectRes.data?.results || subjectRes.data || [];
            const map = {};
            if (Array.isArray(subs)) {
                subs.forEach(s => {
                    map[s.id] = s.name;
                });
            }
            setSubjectsMap(map);
        }).catch(err => {
            console.error("Error loading initial metadata", err);
            setStatusMessage({ type: 'error', text: 'Failed to load initial metadata.' });
        }).finally(() => {
            setIsLoadingData(false);
        });
    }, []);

    // Fetch requirements and existing constraints whenever class/stream changes
    useEffect(() => {
        if (!selectedClass) {
            setRequirements([]);
            setFormState({});
            return;
        }

        setStatusMessage({ type: '', text: '' });

        Promise.all([
            SubjectConstraintService.getRequirements(selectedClass, selectedStream),
            SubjectConstraintService.getConstraints(selectedClass, selectedStream)
        ]).then(([reqRes, constraintRes]) => {
            const reqs = reqRes.data?.results || reqRes.data || [];
            const constraints = constraintRes.data?.results || constraintRes.data || [];
            
            setRequirements(reqs);

            const initialForm = {};
            reqs.forEach(req => {
                const existing = constraints.find(c => c.subject_requirement === req.id || c.subject_requirement_detail?.id === req.id);

                initialForm[req.id] = {
                    priority: existing ? existing.priority : 5,
                    max_periods_per_day: existing ? existing.max_periods_per_day : 1,
                    allow_consecutive_periods: existing ? existing.allow_consecutive_periods : false,
                    required_consecutive_periods: existing ? existing.required_consecutive_periods : 1,
                    spread_across_week: existing ? existing.spread_across_week : true,
                    avoid_first_period: existing ? existing.avoid_first_period : false,
                    avoid_last_period: existing ? existing.avoid_last_period : false,
                    preferred_time_slot: existing ? existing.preferred_time_slot : 'ANY',
                    remarks: existing ? existing.remarks : ''
                };
            });

            setFormState(initialForm);
        }).catch(err => {
            console.error("Error fetching class constraints matrix", err);
            setStatusMessage({ type: 'error', text: 'Failed to load requirements or constraints for this class.' });
        });
    }, [selectedClass, selectedStream]);

    const handleChange = (reqId, field, value) => {
        setStatusMessage({ type: '', text: '' });
        setFormState(prev => ({
            ...prev,
            [reqId]: {
                ...prev[reqId],
                [field]: value
            }
        }));
    };

    const handleSave = async () => {
        if (!selectedClass) {
            setStatusMessage({ type: 'error', text: 'Please select a class first.' });
            return;
        }

        setIsSaving(true);
        setStatusMessage({ type: '', text: '' });

        const constraintsToSave = Object.keys(formState).map(reqId => {
            const item = formState[reqId];
            return {
                subject_requirement_id: parseInt(reqId, 10),
                priority: parseInt(item.priority, 10) || 5,
                max_periods_per_day: parseInt(item.max_periods_per_day, 10) || 1,
                allow_consecutive_periods: !!item.allow_consecutive_periods,
                required_consecutive_periods: parseInt(item.required_consecutive_periods, 10) || 1,
                spread_across_week: !!item.spread_across_week,
                avoid_first_period: !!item.avoid_first_period,
                avoid_last_period: !!item.avoid_last_period,
                preferred_time_slot: item.preferred_time_slot || 'ANY',
                remarks: item.remarks || ''
            };
        });

        const payload = {
            school_class: parseInt(selectedClass, 10),
            stream: selectedStream ? parseInt(selectedStream, 10) : null,
            constraints: constraintsToSave
        };

        try {
            await SubjectConstraintService.saveConstraints(payload);
            setStatusMessage({ type: 'success', text: 'Subject constraints saved successfully!' });
        } catch (error) {
            console.error("Save error:", error);
            setStatusMessage({ type: 'error', text: 'Failed to save constraints. Check fields and try again.' });
        } finally {
            setIsSaving(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-50 p-8 font-sans text-gray-800">
            <div className="mx-auto max-w-7xl bg-white shadow-sm ring-1 ring-gray-900/5 sm:rounded-xl">
                
                <div className="border-b border-gray-200 px-6 py-5 flex items-center justify-between">
                    <div>
                        <h2 className="text-xl font-semibold leading-6 text-gray-900">Configure Subject Constraints</h2>
                        <p className="mt-1 text-sm text-gray-500">Define scheduling limitations, preferred time segments, and spacing parameters.</p>
                    </div>
                </div>

                <div className="px-6 py-6">
                    <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 mb-8">
                        <div>
                            <label className="block text-sm font-medium leading-6 text-gray-900 mb-2">Class <span className="text-red-500">*</span></label>
                            <select 
                                className="block w-full rounded-md border-0 py-1.5 pl-3 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 sm:text-sm bg-white"
                                value={selectedClass} 
                                onChange={e => setSelectedClass(e.target.value)}
                                disabled={isLoadingData}
                            >
                                <option value="" disabled>-- Select Class --</option>
                                {Array.isArray(classes) && classes.map(c => <option key={c.id} value={c.id}>{c.name}</option>)}
                            </select>
                        </div>
                        <div>
                            <label className="block text-sm font-medium leading-6 text-gray-900 mb-2">Stream (Optional)</label>
                            <select 
                                className="block w-full rounded-md border-0 py-1.5 pl-3 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 sm:text-sm bg-white"
                                value={selectedStream} 
                                onChange={e => setSelectedStream(e.target.value)}
                                disabled={isLoadingData}
                            >
                                <option value="">-- No Stream --</option>
                                {Array.isArray(streams) && streams.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}
                            </select>
                        </div>
                    </div>

                    {statusMessage.text && (
                        <div className={`mb-6 rounded-md p-4 text-sm font-medium ${statusMessage.type === 'error' ? 'bg-red-50 text-red-800 ring-1 ring-red-600/20' : 'bg-green-50 text-green-800 ring-1 ring-green-600/20'}`}>
                            {statusMessage.text}
                        </div>
                    )}

                    {!selectedClass ? (
                        <div className="text-center py-12 rounded-lg border-2 border-dashed border-gray-300">
                            <h3 className="text-sm font-semibold text-gray-900">No class selected</h3>
                            <p className="text-sm text-gray-500">Select a class first to view and manage constraints for its assigned subjects.</p>
                        </div>
                    ) : requirements.length === 0 ? (
                        <div className="text-center py-12 rounded-lg border-2 border-dashed border-gray-300">
                            <h3 className="text-sm font-semibold text-gray-900">No subjects assigned</h3>
                            <p className="text-sm text-gray-500">Please assign subjects to this class via the Subject Requirements page first.</p>
                        </div>
                    ) : (
                        <div className="overflow-x-auto shadow ring-1 ring-black ring-opacity-5 sm:rounded-lg">
                            <table className="min-w-full divide-y divide-gray-300 text-left">
                                <thead className="bg-gray-50 text-xs font-semibold uppercase text-gray-700">
                                    <tr>
                                        <th className="py-3.5 pl-4 pr-3 sm:pl-6">Subject</th>
                                        <th className="px-3 py-3.5 text-center">Priority</th>
                                        <th className="px-3 py-3.5 text-center">Max/Day</th>
                                        <th className="px-3 py-3.5 text-center">Consecutive?</th>
                                        <th className="px-3 py-3.5 text-center">Req. Consec.</th>
                                        <th className="px-3 py-3.5 text-center">Spread</th>
                                        <th className="px-3 py-3.5 text-center">Avoid 1st</th>
                                        <th className="px-3 py-3.5 text-center">Avoid Last</th>
                                        <th className="px-3 py-3.5">Time Slot</th>
                                    </tr>
                                </thead>
                                <tbody className="divide-y divide-gray-200 bg-white text-sm">
                                    {requirements.map(req => {
                                        const state = formState[req.id] || {};
                                        // Resolves the name using direct properties or lookup map fallback
                                        const resolvedSubjectName = req.subject_name || 
                                                                   req.subject_detail?.name || 
                                                                   req.subject_requirement_detail?.subject_name || 
                                                                   subjectsMap[req.subject] || 
                                                                   `Subject #${req.subject}`;

                                        return (
                                            <tr key={req.id} className="hover:bg-gray-50">
                                                <td className="py-4 pl-4 pr-3 sm:pl-6 font-medium text-gray-900">
                                                    {resolvedSubjectName}
                                                </td>
                                                <td className="px-3 py-4 text-center">
                                                    <input 
                                                        type="number" min="1" max="10"
                                                        className="w-14 text-center rounded-md border-0 py-1 ring-1 ring-inset ring-gray-300"
                                                        value={state.priority ?? 5}
                                                        onChange={e => handleChange(req.id, 'priority', e.target.value)}
                                                    />
                                                </td>
                                                <td className="px-3 py-4 text-center">
                                                    <input 
                                                        type="number" min="1" max="5"
                                                        className="w-14 text-center rounded-md border-0 py-1 ring-1 ring-inset ring-gray-300"
                                                        value={state.max_periods_per_day ?? 1}
                                                        onChange={e => handleChange(req.id, 'max_periods_per_day', e.target.value)}
                                                    />
                                                </td>
                                                <td className="px-3 py-4 text-center">
                                                    <input 
                                                        type="checkbox"
                                                        className="h-4 w-4 rounded border-gray-300 text-blue-600 cursor-pointer"
                                                        checked={!!state.allow_consecutive_periods}
                                                        onChange={e => handleChange(req.id, 'allow_consecutive_periods', e.target.checked)}
                                                    />
                                                </td>
                                                <td className="px-3 py-4 text-center">
                                                    <input 
                                                        type="number" min="1"
                                                        className="w-14 text-center rounded-md border-0 py-1 ring-1 ring-inset ring-gray-300"
                                                        value={state.required_consecutive_periods ?? 1}
                                                        onChange={e => handleChange(req.id, 'required_consecutive_periods', e.target.value)}
                                                    />
                                                </td>
                                                <td className="px-3 py-4 text-center">
                                                    <input 
                                                        type="checkbox"
                                                        className="h-4 w-4 rounded border-gray-300 text-blue-600 cursor-pointer"
                                                        checked={!!state.spread_across_week}
                                                        onChange={e => handleChange(req.id, 'spread_across_week', e.target.checked)}
                                                    />
                                                </td>
                                                <td className="px-3 py-4 text-center">
                                                    <input 
                                                        type="checkbox"
                                                        className="h-4 w-4 rounded border-gray-300 text-blue-600 cursor-pointer"
                                                        checked={!!state.avoid_first_period}
                                                        onChange={e => handleChange(req.id, 'avoid_first_period', e.target.checked)}
                                                    />
                                                </td>
                                                <td className="px-3 py-4 text-center">
                                                    <input 
                                                        type="checkbox"
                                                        className="h-4 w-4 rounded border-gray-300 text-blue-600 cursor-pointer"
                                                        checked={!!state.avoid_last_period}
                                                        onChange={e => handleChange(req.id, 'avoid_last_period', e.target.checked)}
                                                    />
                                                </td>
                                                <td className="px-3 py-4">
                                                    <select 
                                                        className="rounded-md border-0 py-1 px-2 text-xs ring-1 ring-inset ring-gray-300 bg-white"
                                                        value={state.preferred_time_slot || 'ANY'}
                                                        onChange={e => handleChange(req.id, 'preferred_time_slot', e.target.value)}
                                                    >
                                                        <option value="ANY">Any</option>
                                                        <option value="MORNING">Morning</option>
                                                        <option value="AFTERNOON">Afternoon</option>
                                                    </select>
                                                </td>
                                            </tr>
                                        );
                                    })}
                                </tbody>
                            </table>
                            
                            <div className="bg-gray-50 px-6 py-4 flex justify-end border-t border-gray-200">
                                <button
                                    type="button"
                                    onClick={handleSave}
                                    disabled={isSaving}
                                    className="rounded-md bg-blue-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-blue-500 disabled:opacity-50"
                                >
                                    {isSaving ? 'Saving Constraints...' : 'Save Constraints'}
                                </button>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default SubjectConstraintListPage;