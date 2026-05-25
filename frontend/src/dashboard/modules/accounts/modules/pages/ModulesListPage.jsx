// src/modules/accounts/modules/pages/ModuleListPage.jsx

import {
    useEffect,
    useState,
} from "react";

import {
    Link,
} from "react-router-dom";

import {
    getModules,
    deleteModule,
} from "../services/moduleService";


export default function ModuleListPage() {

    const [modules, setModules] = useState([]);

    const loadModules = async () => {

        try {

            const data = await getModules();

            setModules(data);

        } catch (error) {

            console.error(error);
        }
    };

    useEffect(() => {

        loadModules();

    }, []);

    const handleDelete = async (id) => {

        const confirmDelete = window.confirm(
            "Are you sure?"
        );

        if (!confirmDelete) return;

        try {

            await deleteModule(id);

            loadModules();

        } catch (error) {

            console.error(error);
        }
    };

    return (

        <div className="p-6">

            <div className="flex justify-between mb-6">

                <h1 className="text-2xl font-bold">
                    Modules
                </h1>

                <Link
                    to="/dashboard/modules/add"
                    className="bg-blue-600 text-white px-4 py-2 rounded"
                >
                    Add Module
                </Link>

            </div>

            <table className="w-full border">

                <thead>

                    <tr className="bg-gray-100">

                        <th className="p-3 border">
                            ID
                        </th>

                        <th className="p-3 border">
                            Name
                        </th>

                        <th className="p-3 border">
                            Slug
                        </th>

                        <th className="p-3 border">
                            Status
                        </th>

                        <th className="p-3 border">
                            Actions
                        </th>

                    </tr>

                </thead>

                <tbody>

                    {modules.map((module) => (

                        <tr key={module.id}>

                            <td className="p-3 border">
                                {module.id}
                            </td>

                            <td className="p-3 border">
                                {module.name}
                            </td>

                            <td className="p-3 border">
                                {module.slug}
                            </td>

                            <td className="p-3 border">

                                {module.is_active
                                    ? "Active"
                                    : "Inactive"}

                            </td>

                            <td className="p-3 border flex gap-2">

                                <Link
                                    to={`/dashboard/modules/edit/${module.id}`}
                                    className="bg-yellow-500 text-white px-3 py-1 rounded"
                                >
                                    Edit
                                </Link>

                                <button
                                    onClick={() => handleDelete(module.id)}
                                    className="bg-red-600 text-white px-3 py-1 rounded"
                                >
                                    Delete
                                </button>

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>
    );
}