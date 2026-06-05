import React from "react";

const RollCallFilters = ({

    filters,

    selectedClass,

    selectedSection,

    setSelectedClass,

    setSelectedSection,

    handleSearch,

}) => {

    return (

        <div className="flex gap-4 mb-6">

            <select
                value={selectedClass}
                onChange={(e) =>
                    setSelectedClass(
                        e.target.value
                    )
                }
                className="
                    border
                    px-3
                    py-2
                    rounded
                "
            >

                <option value="">
                    Select Class
                </option>

                {(filters.classes || []).map(
                    (item) => (

                        <option
                            key={item}
                            value={item}
                        >
                            {item}
                        </option>

                    )
                )}

            </select>

            <select
                value={selectedSection}
                onChange={(e) =>
                    setSelectedSection(
                        e.target.value
                    )
                }
                className="
                    border
                    px-3
                    py-2
                    rounded
                "
            >

                <option value="">
                    Select Section
                </option>

                {(filters.sections || []).map(
                    (item) => (

                        <option
                            key={item}
                            value={item}
                        >
                            {item}
                        </option>

                    )
                )}

            </select>

            <button
                onClick={handleSearch}
                className="
                    bg-blue-600
                    text-white
                    px-4
                    py-2
                    rounded
                "
            >
                Search
            </button>

        </div>

    );

};

export default RollCallFilters;