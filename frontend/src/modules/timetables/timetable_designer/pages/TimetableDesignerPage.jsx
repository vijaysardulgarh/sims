import {
    useState,
    useEffect,
} from 'react';

import {
    DndContext,
} from '@dnd-kit/core';

import TimetableGrid
    from '../components/TimetableGrid';

import TimetableToolbar
    from '../components/TimetableToolbar';

import ConflictPanel
    from '../components/ConflictPanel';

import SubjectPalette
    from '../components/SubjectPalette';

import TeacherPalette
    from '../components/TeacherPalette';

import RoomPalette
    from '../components/RoomPalette';

import timetableDesignerService
    from '../services/timetableDesignerService';

import subjectPaletteService
    from '../services/subjectPaletteService';

import teacherPaletteService
    from '../services/teacherPaletteService';

import roomPaletteService
    from '../services/roomPaletteService';

const TimetableDesignerPage = () => {

    const [
        entries,
        setEntries,
    ] = useState([]);

    const [
        conflicts,
        setConflicts,
    ] = useState([]);

    const [
        subjects,
        setSubjects,
    ] = useState([]);

    const [
        teachers,
        setTeachers,
    ] = useState([]);

    const [
        rooms,
        setRooms,
    ] = useState([]);

    const loadGrid =
        async () => {

            try {

                const response =

                    await timetableDesignerService
                        .getGrid(
                            1
                        );

                setEntries(
                    response.data
                );

            }

            catch (
                error
            ) {

                console.error(
                    error
                );

            }

        };

    const loadConflicts =
        async () => {

            try {

                const response =

                    await timetableDesignerService
                        .getConflicts();

                setConflicts(
                    response.data
                );

            }

            catch (
                error
            ) {

                console.error(
                    error
                );

            }

        };

    const loadSubjects =
        async () => {

            try {

                const response =

                    await subjectPaletteService
                        .getAll();

                setSubjects(

                    response.data.results ||

                    response.data

                );

            }

            catch (
                error
            ) {

                console.error(
                    error
                );

            }

        };

    const loadTeachers =
        async () => {

            try {

                const response =

                    await teacherPaletteService
                        .getAll();

                setTeachers(

                    response.data.results ||

                    response.data

                );

            }

            catch (
                error
            ) {

                console.error(
                    error
                );

            }

        };

    const loadRooms =
        async () => {

            try {

                const response =

                    await roomPaletteService
                        .getAll();

                setRooms(

                    response.data.results ||

                    response.data

                );

            }

            catch (
                error
            ) {

                console.error(
                    error
                );

            }

        };

    const handleGenerate =
        async () => {

            try {

                await timetableDesignerService
                    .generate(
                        1
                    );

                await loadGrid();

                await loadConflicts();

            }

            catch (
                error
            ) {

                console.error(
                    error
                );

            }

        };

const handleDragEnd =
    async (
        event
    ) => {

        const {
            active,
            over,
        } = event;

        if (
            !over
        ) {

            return;

        }

        const activeData =
            active.data.current;

        const targetEntryId =
            over.data.current?.entryId;

        try {

            if (
                activeData.type ===
                'subject'
            ) {

                await timetableDesignerService
                    .assignSubject({

                        entry_id:
                            targetEntryId,

                        subject_id:
                            activeData.subject.id,

                    });

            }

            else if (
                activeData.type ===
                'teacher'
            ) {

                await timetableDesignerService
                    .assignTeacher({

                        entry_id:
                            targetEntryId,

                        teacher_id:
                            activeData.teacher.id,

                    });

            }

            else if (
                activeData.type ===
                'room'
            ) {

                await timetableDesignerService
                    .assignRoom({

                        entry_id:
                            targetEntryId,

                        room_id:
                            activeData.room.id,

                    });

            }

            else if (
                activeData.type ===
                'entry'
            ) {

                const [
                    ,
                    day,
                    period,
                ] = over.id.split(
                    '-'
                );

                await timetableDesignerService
                    .moveEntry({

                        entry_id:
                            activeData.entry.id,

                        day,

                        period:
                            Number(
                                period
                            ),

                    });

            }

            await loadGrid();

            await loadConflicts();

        }

        catch (
            error
        ) {

            console.error(
                error
            );

        }

    };

    useEffect(
        () => {

            loadGrid();

            loadConflicts();

            loadSubjects();

            loadTeachers();

            loadRooms();

        },
        []
    );

return (

    <DndContext

        onDragStart={(event) => {

            console.log(
                'DRAG START',
                event
            );

        }}

        onDragMove={(event) => {

            console.log(
                'DRAG MOVE',
                event
            );

        }}

        onDragOver={(event) => {

            console.log(
                'DRAG OVER',
                event
            );

        }}

        onDragEnd={(event) => {

            console.log(
                'DRAG END',
                event
            );

            handleDragEnd(
                event
            );

        }}

        onDragCancel={(event) => {

            console.log(
                'DRAG CANCEL',
                event
            );

        }}

    >

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

            <div
                className="
                    grid
                    grid-cols-12
                    gap-4
                "
            >

                <div
                    className="
                        col-span-3
                        space-y-4
                    "
                >

                    <SubjectPalette
                        subjects={
                            subjects
                        }
                    />

                    <TeacherPalette
                        teachers={
                            teachers
                        }
                    />

                    <RoomPalette
                        rooms={
                            rooms
                        }
                    />

                </div>

                <div
                    className="
                        col-span-9
                    "
                >

                    <TimetableGrid
                        entries={
                            entries
                        }
                    />

                </div>

            </div>

            <ConflictPanel
                conflicts={
                    conflicts
                }
            />

        </div>

    </DndContext>

);

};

export default TimetableDesignerPage;