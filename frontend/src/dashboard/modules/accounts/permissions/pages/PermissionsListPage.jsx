import {

    useEffect,

    useState

} from "react";

import {

    Link

} from "react-router-dom";

import accessControlService from "./accessControlService";


const AccessControlListPage = () => {

    const [accessControls, setAccessControls] =
        useState([]);


    // =====================================
    // FETCH ACCESS CONTROLS
    // =====================================

    useEffect(() => {

        fetchAccessControls();

    }, []);


    const fetchAccessControls = async () => {

        try {

            const data =
                await accessControlService.getAccessControls();

            setAccessControls(data);

        } catch (error) {

            console.error(
                "Fetch Access Controls Error:",
                error
            );
        }
    };


    // =====================================
    // DELETE ACCESS CONTROL
    // =====================================

    const handleDelete = async (
        id
    ) => {

        const confirmDelete = window.confirm(

            "Delete access control?"
        );

        if (!confirmDelete) return;

        try {

            await accessControlService.deleteAccessControl(
                id
            );

            fetchAccessControls();

        } catch (error) {

            console.error(
                "Delete Access Control Error:",
                error
            );
        }
    };


    return (

        <div className="p-4">

            {/* ================================= */}
            {/* HEADER */}
            {/* ================================= */}

            <div className="flex justify-between items-center mb-4">

                <h1 className="text-2xl font-bold">

                    Access Controls

                </h1>

                <Link
                    to="/dashboard/access-controls/add"
                    className="bg-blue-600 text-white px-4 py-2 rounded"
                >

                    Add Access Control

                </Link>

            </div>


            {/* ================================= */}
            {/* TABLE */}
            {/* ================================= */}

            <div className="overflow-x-auto">

                <table className="w-full border">

                    <thead>

                        <tr className="bg-gray-100">

                            <th className="border p-2">
                                ID
                            </th>

                            <th className="border p-2">
                                Name
                            </th>

                            <th className="border p-2">
                                Code
                            </th>

                            <th className="border p-2">
                                Module
                            </th>

                            <th className="border p-2">
                                Actions
                            </th>

                        </tr>

                    </thead>


                    <tbody>

                        {
                            accessControls.length > 0 ? (

                                accessControls.map((item) => (

                                    <tr key={item.id}>

                                        <td className="border p-2">

                                            {item.id}

                                        </td>

                                        <td className="border p-2">

                                            {item.name}

                                        </td>

                                        <td className="border p-2">

                                            {item.code}

                                        </td>

                                        <td className="border p-2">

                                            {item.module}

                                        </td>

                                        <td className="border p-2 flex gap-2">

                                            <Link
                                                to={`/dashboard/access-controls/edit/${item.id}`}
                                                className="bg-yellow-500 text-white px-3 py-1 rounded"
                                            >

                                                Edit

                                            </Link>

                                            <button
                                                onClick={() =>
                                                    handleDelete(item.id)
                                                }
                                                className="bg-red-600 text-white px-3 py-1 rounded"
                                            >

                                                Delete

                                            </button>

                                        </td>

                                    </tr>
                                ))

                            ) : (

                                <tr>

                                    <td
                                        colSpan="5"
                                        className="border p-4 text-center"
                                    >

                                        No Access Controls Found

                                    </td>

                                </tr>
                            )
                        }

                    </tbody>

                </table>

            </div>

        </div>
    );
};

export default AccessControlListPage;