import {
    useEffect,
    useState,
} from "react";

import {
    getRollCallFilters,
    getRollCallReport,
} from "../services/rollCallService";

import RollCallFilters
from "../components/RollCallFilters";

import RollCallActions
from "../components/RollCallActions";

import RollCallTable
from "../components/RollCallTable";

const RollCallReportPage = () => {

    const [filters, setFilters] =
        useState({
            classes: [],
            sections: [],
        });

    const [selectedClass, setSelectedClass] =
        useState("");

    const [selectedSection, setSelectedSection] =
        useState("");

    const [report, setReport] =
        useState(null);

    useEffect(() => {

        loadFilters();

    }, []);

    const loadFilters = async () => {

        try {

            const response =
                await getRollCallFilters();

            setFilters(
                response.data
            );

        } catch (error) {

            console.error(error);

        }

    };

    const handleSearch = async () => {

        try {

            const response =
                await getRollCallReport({

                    class: selectedClass,
                    section: selectedSection,

                });

            setReport(
                response.data
            );

        } catch (error) {

            console.error(error);

        }

    };

    return (

        <div className="p-6">

            <h1 className="text-2xl font-bold mb-6">

                Roll Call Report

            </h1>

            <RollCallFilters

                filters={filters}

                selectedClass={selectedClass}

                selectedSection={selectedSection}

                setSelectedClass={setSelectedClass}

                setSelectedSection={setSelectedSection}

                handleSearch={handleSearch}

            />

            {report && (

                <>

                    <RollCallActions

                        selectedClass={
                            selectedClass
                        }

                        selectedSection={
                            selectedSection
                        }

                    />

                    <RollCallTable
                        report={report}
                    />

                </>

            )}

        </div>

    );

};

export default RollCallReportPage;