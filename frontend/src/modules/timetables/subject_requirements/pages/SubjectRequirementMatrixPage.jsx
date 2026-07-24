import React, { useState, useEffect } from 'react';
import { SubjectRequirementService } from "../services/subjectRequirementService";

const SubjectRequirementListPage = () => {
    const [classes, setClasses] = useState([]);
    const [streams, setStreams] = useState([]);
    const [subjects, setSubjects] = useState([]);
    
    const [selectedClass, setSelectedClass] = useState('');
    const [selectedStream, setSelectedStream] = useState('');
    
    // Form state: { subjectId: { assigned: bool, theory: number, lab: number, ... } }
    const [formState, setFormState] = useState({});
    
    // UI Feedback states
    const [isSaving, setIsSaving] = useState(false);
    const [statusMessage, setStatusMessage] = useState({ type: '', text: '' });
    const [isLoadingData, setIsLoadingData] = useState(true);

    // Fetch initial dropdown data with bulletproof array checking
    useEffect(() => {
        setIsLoadingData(true);
        Promise.all([
            SubjectRequirementService.getClasses(),
            SubjectRequirementService.getStreams(),
            SubjectRequirementService.getSubjects()
        ]).then(([classRes, streamRes, subjectRes]) => {
            // Safely resolve whether data is directly an array or nested under .results
            const classData = classRes.data?.results || classRes.data || [];
            const streamData = streamRes.data?.results || streamRes.data || [];
            const subjectData = subjectRes.data?.results || subjectRes.data || [];

            setClasses(Array.isArray(classData) ? classData : []);
            setStreams(Array.isArray(streamData) ? streamData : []);
            setSubjects(Array.isArray(subjectData) ? subjectData : []);
        }).catch(err => {
            console.error("Error fetching initial dropdown data", err);
            setClasses([]);
            setStreams([]);
            setSubjects([]);
            setStatusMessage({ type: 'error', text: 'Failed to load classes and streams from backend.' });
        }).finally(() => {
            setIsLoadingData(false);
        });
    }, []);

    // Fetch requirements when Class or Stream changes
    useEffect(() => {
        if (!selectedClass) return;

        setStatusMessage({ type: '', text: '' });

        SubjectRequirementService.getRequirements(selectedClass, selectedStream)
            .then(res => {
                const existingReqs = res.data?.results || res.data || [];
                const newFormState = {};
                
                // Initialize all subjects as unassigned by default
                if (Array.isArray(subjects)) {
                    subjects.forEach(sub => {
                        newFormState[sub.id] = { 
                            assigned: false, 
                            theory: '', 
                            lab: '', 
                            is_compulsory: true, 
                            is_shared: false, 
                            priority: 0 
                        };
                    });
                }

                // Overwrite with existing assignments found in the database
                if (Array.isArray(existingReqs)) {
                    existingReqs.forEach(req => {
                        if (newFormState[req.subject]) {
                            newFormState[req.subject] = {
                                assigned: true,
                                theory: req.theory_periods_per_week,
                                lab: req.lab_periods_per_week,
                                is_compulsory: req.is_compulsory ?? true,
                                is_shared: req.is_shared ?? false,
                                priority: req.priority || 0
                            };
                        }
                    });
                }

                setFormState(newFormState);
            })
            .catch(err => {
                console.error("Error fetching requirements", err);
                setStatusMessage({ type: 'error', text: 'Failed to fetch existing requirements for this class.' });
            });
    }, [selectedClass, selectedStream, subjects]);

    const handleCheckboxToggle = (subjectId, field) => {
        setStatusMessage({ type: '', text: '' });
        setFormState(prev => {
            const current = prev[subjectId] || { assigned: false, theory: '', lab: '', is_compulsory: true, is_shared: false, priority: 0 };
            
            let updatedAssigned = current.assigned;
            if (field === 'assigned') {
                updatedAssigned = !current.assigned;
            }

            return {
                ...prev,
                [subjectId]: {
                    ...current,
                    [field]: field === 'assigned' ? updatedAssigned : !current[field],
                    theory: field === 'assigned' && updatedAssigned && !current.theory ? 0 : current.theory,
                    lab: field === 'assigned' && updatedAssigned && !current.lab ? 0 : current.lab,
                }
            };
        });
    };

    const handleInputChange = (subjectId, field, value) => {
        setStatusMessage({ type: '', text: '' });
        setFormState(prev => ({
            ...prev,
            [subjectId]: {
                ...prev[subjectId],
                [field]: value === '' ? '' : Math.max(0, parseInt(value, 10))
            }
        }));
    };

    const handleSave = async () => {
        if (!selectedClass) {
            setStatusMessage({ type: 'error', text: 'Please select a class before saving.' });
            return;
        }

        setIsSaving(true);
        setStatusMessage({ type: '', text: '' });

        const requirementsToSave = Object.keys(formState)
            .filter(subjectId => formState[subjectId].assigned)
            .map(subjectId => {
                const item = formState[subjectId];
                return {
                    subject_id: parseInt(subjectId, 10),
                    theory_periods_per_week: item.theory === '' ? 0 : parseInt(item.theory, 10),
                    lab_periods_per_week: item.lab === '' ? 0 : parseInt(item.lab, 10),
                    is_compulsory: item.is_compulsory,
                    is_shared: item.is_shared,
                    priority: item.priority === '' ? 0 : parseInt(item.priority, 10)
                };
            });

        const payload = {
            school_class: parseInt(selectedClass, 10),
            stream: selectedStream ? parseInt(selectedStream, 10) : null,
            requirements: requirementsToSave
        };

        try {
            await SubjectRequirementService.saveRequirements(payload);
            setStatusMessage({ type: 'success', text: 'Requirements saved successfully!' });
        } catch (error) {
            console.error("Save error:", error);
            setStatusMessage({ type: 'error', text: 'Failed to save requirements. Please try again.' });
        } finally {
            setIsSaving(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-50 p-8 font-sans text-gray-800">
            <div className="mx-auto max-w-7xl bg-white shadow-sm ring-1 ring-gray-900/5 sm:rounded-xl">
                
                <div className="border-b border-gray-200 px-6 py-5 flex items-center justify-between">
                    <div>
                        <h2 className="text-xl font-semibold leading-6 text-gray-900">Assign Subjects to Class</h2>
                        <p className="mt-1 text-sm text-gray-500">Manage subject allocations, periods, and attributes for each class and stream.</p>
                    </div>
                </div>

                <div className="px-6 py-6">
                    {/* Dropdown Filters Section */}
                    <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 mb-8">
                        <div>
                            <label className="block text-sm font-medium leading-6 text-gray-900 mb-2">Class <span className="text-red-500">*</span></label>
                            <select 
                                className="block w-full rounded-md border-0 py-1.5 pl-3 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-blue-600 sm:text-sm bg-white"
                                value={selectedClass} 
                                onChange={e => setSelectedClass(e.target.value)}
                                disabled={isLoadingData}
                            >
                                <option value="" disabled>-- Select Class --</option>
                                {Array.isArray(classes) && classes.map(c => (
                                    <option key={c.id} value={c.id}>{c.name}</option>
                                ))}
                            </select>
                        </div>
                        <div>
                            <label className="block text-sm font-medium leading-6 text-gray-900 mb-2">Stream (Optional)</label>
                            <select 
                                className="block w-full rounded-md border-0 py-1.5 pl-3 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-blue-600 sm:text-sm bg-white"
                                value={selectedStream} 
                                onChange={e => setSelectedStream(e.target.value)}
                                disabled={isLoadingData}
                            >
                                <option value="">-- No Stream --</option>
                                {Array.isArray(streams) && streams.map(s => (
                                    <option key={s.id} value={s.id}>{s.name}</option>
                                ))}
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
                            <p className="text-sm text-gray-500">Please select a class from the dropdown above to manage subject requirements.</p>
                        </div>
                    ) : (
                        <div className="overflow-x-auto shadow ring-1 ring-black ring-opacity-5 sm:rounded-lg">
                            <table className="min-w-full divide-y divide-gray-300">
                                <thead className="bg-gray-50 text-xs font-semibold uppercase text-gray-700">
                                    <tr>
                                        <th className="py-3.5 pl-4 pr-3 text-left sm:pl-6 w-20">Assign</th>
                                        <th className="px-3 py-3.5 text-left">Subject Name</th>
                                        <th className="px-3 py-3.5 text-center w-28">Theory</th>
                                        <th className="px-3 py-3.5 text-center w-28">Lab</th>
                                        <th className="px-3 py-3.5 text-center w-28">Compulsory</th>
                                        <th className="px-3 py-3.5 text-center w-28">Shared</th>
                                        <th className="px-3 py-3.5 text-center w-24">Priority</th>
                                        <th className="py-3.5 pl-3 pr-4 text-right sm:pr-6 w-28">Status</th>
                                    </tr>
                                </thead>
                                <tbody className="divide-y divide-gray-200 bg-white text-sm">
                                    {Array.isArray(subjects) && subjects.map(subject => {
                                        const rowState = formState[subject.id] || { assigned: false, theory: '', lab: '', is_compulsory: true, is_shared: false, priority: 0 };
                                        const isDisabled = !rowState.assigned;

                                        return (
                                            <tr key={subject.id} className={isDisabled ? 'bg-gray-50/50' : 'hover:bg-gray-50'}>
                                                <td className="py-4 pl-4 pr-3 sm:pl-6">
                                                    <input 
                                                        type="checkbox" 
                                                        className="h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-600 cursor-pointer"
                                                        checked={rowState.assigned} 
                                                        onChange={() => handleCheckboxToggle(subject.id, 'assigned')} 
                                                    />
                                                </td>
                                                <td className={`font-medium ${isDisabled ? 'text-gray-400' : 'text-gray-900'}`}>
                                                    {subject.name}
                                                </td>
                                                <td className="px-3 py-4 text-center">
                                                    <input 
                                                        type="number" min="0" disabled={isDisabled}
                                                        className="w-16 mx-auto rounded-md border-0 py-1 text-center ring-1 ring-inset ring-gray-300 disabled:bg-gray-100 disabled:text-gray-400"
                                                        value={rowState.theory}
                                                        onChange={e => handleInputChange(subject.id, 'theory', e.target.value)}
                                                    />
                                                </td>
                                                <td className="px-3 py-4 text-center">
                                                    <input 
                                                        type="number" min="0" disabled={isDisabled}
                                                        className="w-16 mx-auto rounded-md border-0 py-1 text-center ring-1 ring-inset ring-gray-300 disabled:bg-gray-100 disabled:text-gray-400"
                                                        value={rowState.lab}
                                                        onChange={e => handleInputChange(subject.id, 'lab', e.target.value)}
                                                    />
                                                </td>
                                                <td className="px-3 py-4 text-center">
                                                    <input 
                                                        type="checkbox" disabled={isDisabled}
                                                        className="h-4 w-4 rounded border-gray-300 text-blue-600 cursor-pointer disabled:opacity-50"
                                                        checked={rowState.is_compulsory}
                                                        onChange={() => handleCheckboxToggle(subject.id, 'is_compulsory')}
                                                    />
                                                </td>
                                                <td className="px-3 py-4 text-center">
                                                    <input 
                                                        type="checkbox" disabled={isDisabled}
                                                        className="h-4 w-4 rounded border-gray-300 text-blue-600 cursor-pointer disabled:opacity-50"
                                                        checked={rowState.is_shared}
                                                        onChange={() => handleCheckboxToggle(subject.id, 'is_shared')}
                                                    />
                                                </td>
                                                <td className="px-3 py-4 text-center">
                                                    <input 
                                                        type="number" min="0" disabled={isDisabled}
                                                        className="w-14 mx-auto rounded-md border-0 py-1 text-center ring-1 ring-inset ring-gray-300 disabled:bg-gray-100 disabled:text-gray-400"
                                                        value={rowState.priority}
                                                        onChange={e => handleInputChange(subject.id, 'priority', e.target.value)}
                                                    />
                                                </td>
                                                <td className="py-4 pl-3 pr-4 text-right sm:pr-6">
                                                    {isDisabled ? (
                                                        <span className="inline-flex items-center rounded-full bg-gray-100 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10">Disabled</span>
                                                    ) : (
                                                        <span className="inline-flex items-center rounded-full bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20">Active</span>
                                                    )}
                                                </td>
                                            </tr>
                                        );
                                    })}
                                </tbody>
                            </table>
                            
                            <div className="bg-gray-50 px-6 py-4 flex items-center justify-end border-t border-gray-200">
                                <button
                                    type="button"
                                    onClick={handleSave}
                                    disabled={isSaving}
                                    className="inline-flex items-center justify-center rounded-md bg-blue-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-blue-500 disabled:opacity-50"
                                >
                                    {isSaving ? 'Saving...' : 'Save Requirements'}
                                </button>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default SubjectRequirementListPage;