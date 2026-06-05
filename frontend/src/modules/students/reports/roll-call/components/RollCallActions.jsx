import React from "react";

import {
    useNavigate,
} from "react-router-dom";

const RollCallActions = ({

    selectedClass,

    selectedSection,

}) => {

    const navigate =
        useNavigate();

    const handlePrint = () => {

        if (
            !selectedClass ||
            !selectedSection
        ) {

            alert(
                "Please select Class and Section first."
            );

            return;

        }

        window.open(
            `/print/roll-call?class=${selectedClass}&section=${selectedSection}`,
            "_blank"
        );

    };

    return (

        <div className="flex gap-3 mb-4">

            <button
                className="
                    bg-green-600
                    text-white
                    px-4
                    py-2
                    rounded
                    hover:bg-green-700
                "
            >

                Excel

            </button>

            <button
                className="
                    bg-red-600
                    text-white
                    px-4
                    py-2
                    rounded
                    hover:bg-red-700
                "
            >

                PDF

            </button>

            <button
                onClick={handlePrint}
                className="
                    bg-gray-800
                    text-white
                    px-4
                    py-2
                    rounded
                    hover:bg-gray-900
                "
            >

                Print

            </button>

        </div>

    );

};

export default RollCallActions;