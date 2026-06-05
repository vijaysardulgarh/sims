import React from "react";

const RollCallTable = ({
    report,
}) => {

    return (

        <div className="bg-white rounded-lg shadow border">

            <div className="p-4 border-b">

                <h2 className="text-xl font-bold">

                    {report.school_name}

                </h2>

                <p className="text-gray-600 mt-1">

                    Class: {report.class_name}
                    {" | "}
                    Section: {report.section_name}
                    {" | "}
                    Total Students: {report.total_students}

                </p>

            </div>

            <div className="overflow-x-auto">

                <table className="w-full border-collapse">

                    <thead>

                        <tr className="bg-gray-100">

                            <th className="border p-2">
                                SRN
                            </th>

                            <th className="border p-2">
                                Roll No
                            </th>

                            <th className="border p-2">
                                Student Name
                            </th>

                            <th className="border p-2">
                                Father Name
                            </th>

                            <th className="border p-2">
                                Mobile
                            </th>

                            <th className="border p-2">
                                Category
                            </th>

                        </tr>

                    </thead>

                    <tbody>

                        {report.students?.length > 0 ? (

                            report.students.map(
                                (
                                    student,
                                    index
                                ) => (

                                    <tr
                                        key={
                                            student.srn ||
                                            index
                                        }
                                    >

                                        <td className="border p-2">
                                            {student.srn}
                                        </td>

                                        <td className="border p-2">
                                            {student.roll_number}
                                        </td>

                                        <td className="border p-2">
                                            {student.full_name_aadhar}
                                        </td>

                                        <td className="border p-2">
                                            {student.father_full_name_aadhar}
                                        </td>

                                        <td className="border p-2">
                                            {student.father_mobile}
                                        </td>

                                        <td className="border p-2">
                                            {student.category}
                                        </td>

                                    </tr>

                                )
                            )

                        ) : (

                            <tr>

                                <td
                                    colSpan="6"
                                    className="
                                        border
                                        p-4
                                        text-center
                                        text-gray-500
                                    "
                                >

                                    No students found

                                </td>

                            </tr>

                        )}

                    </tbody>

                </table>

            </div>

        </div>

    );

};

export default RollCallTable;