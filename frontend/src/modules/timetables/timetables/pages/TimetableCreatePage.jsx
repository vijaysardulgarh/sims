import {
    useEffect,
    useState,
} from 'react';

import api
    from '../../../../services/api/axios';

import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import TimetableForm
    from '../components/TimetableForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/timetableService';

const TimetableCreatePage = () => {

    const [
        academicSessions,
        setAcademicSessions,
    ] = useState([]);

    const [
        classes,
        setClasses,
    ] = useState([]);

    const [
        sections,
        setSections,
    ] = useState([]);

    const [
        bellSchedules,
        setBellSchedules,
    ] = useState([]);

    useEffect(() => {

        loadLookups();

    }, []);

    const loadLookups =
        async () => {

            try {

                const [

                    academicSessionResponse,

                    classResponse,

                    sectionResponse,

                    bellScheduleResponse,

                ] = await Promise.all([

                    api.get(
                        '/academics/sessions/'
                    ),

                    api.get(
                        '/academics/classes/'
                    ),

                    api.get(
                        '/academics/sections/'
                    ),

                    api.get(
                        '/timetables/bell-schedules/'
                    ),

                ]);

                setAcademicSessions(
                    academicSessionResponse.data.results
                    ||
                    academicSessionResponse.data
                );

                setClasses(
                    classResponse.data.results
                    ||
                    classResponse.data
                );

                setSections(
                    sectionResponse.data.results
                    ||
                    sectionResponse.data
                );

                setBellSchedules(
                    bellScheduleResponse.data.results
                    ||
                    bellScheduleResponse.data
                );

            }

            catch (error) {

                console.error(
                    error
                );

            }

        };

    return (

        <CrudCreatePage

            title="Create Timetable"

            endpoint={ENDPOINT}

            FormComponent={
                TimetableForm
            }

            redirectPath={
                LIST_PATH
            }

            formProps={{

                academicSessions,

                classes,

                sections,

                bellSchedules,

            }}

        />

    );

};

export default TimetableCreatePage;