import {
    useEffect,
    useState,
} from "react";

import {
    useSearchParams,
} from "react-router-dom";

import {
    getRollCallReport,
} from "../services/rollCallService";

import RollCallTable
from "../components/RollCallTable";

const RollCallPrintPage = () => {

    const [
        searchParams,
    ] = useSearchParams();

    const [report, setReport] =
        useState(null);

    const selectedClass =
        searchParams.get(
            "class"
        );

    const selectedSection =
        searchParams.get(
            "section"
        );

    useEffect(() => {

        loadReport();

    }, []);

    const loadReport = async () => {

        try {

            const response =
                await getRollCallReport({

                    class:
                        selectedClass,

                    section:
                        selectedSection,

                });

            setReport(
                response.data
            );

        } catch (error) {

            console.error(error);

        }

    };

    useEffect(() => {

        if (report) {

            setTimeout(() => {

                window.print();

            }, 500);

        }

    }, [report]);

    return (

        <div className="p-6 bg-white min-h-screen">

            {report && (

                <RollCallTable
                    report={report}
                />

            )}

        </div>

    );

};

export default RollCallPrintPage;