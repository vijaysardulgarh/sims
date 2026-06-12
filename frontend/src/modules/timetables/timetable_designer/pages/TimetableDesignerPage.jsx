import {
    useState,
} from 'react';

import TimetableGrid
    from '../components/TimetableGrid';

import TimetableToolbar
    from '../components/TimetableToolbar';

import ConflictPanel
    from '../components/ConflictPanel';

import timetableDesignerService
    from '../services/timetableDesignerService';

const TimetableDesignerPage = () => {

    const [entries] =
        useState([]);

    const [conflicts] =
        useState([]);

    const handleGenerate =
        async () => {

            await timetableDesignerService
                .generate(
                    1
                );

        };

    return (

        <div
            className="
                space-y-6
            "
        >

            <h1
                className="
                    text-3xl
                    font-bold
                "
            >
                Timetable Designer
            </h1>

            <TimetableToolbar
                onGenerate={
                    handleGenerate
                }
            />

            <TimetableGrid
                entries={entries}
            />

            <ConflictPanel
                conflicts={conflicts}
            />

        </div>

    );

};

export default TimetableDesignerPage;