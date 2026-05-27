// src/modules/accounts/modules/pages/ModuleListPage.jsx

import React, {
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

    // =====================================
    // STATE
    // =====================================

    const [modules, setModules] = useState([]);

    // =====================================
    // LOAD MODULES
    // =====================================

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

    // =====================================
    // DELETE MODULE
    // =====================================

    const handleDelete = async (id) => {

        const confirmDelete = window.confirm(
            "Are you sure you want to delete this module?"
        );

        if (!confirmDelete) return;

        try {

            await deleteModule(id);

            loadModules();

        } catch (error) {

            console.error(error);
        }
    };

    // =====================================
    // RENDER CHILD MODULES
    // =====================================

    const renderChildren = (
        children = [],
        level = 1
    ) => {

        return children.map((child) => (

            <React.Fragment key={child.id}>

                <tr
                    className="hover:bg-gray-50"
                >

                    <td className="p-3 border">
                        {child.id}
                    </td>

                    <td className="p-3 border">

                        <div
                            style={{
                                paddingLeft: `${level * 20}px`,
                            }}
                            className="flex items-center gap-2"
                        >

                            <span>
                                ↳
                            </span>

                            <span>
                                {child.name}
                            </span>

                        </div>

                    </td>

                    <td className="p-3 border">
                        {child.slug}
                    </td>

                    <td className="p-3 border">
                        {child.path || "-"}
                    </td>

                    <td className="p-3 border">
                        {child.icon || "-"}
                    </td>

                    <td className="p-3 border">
                        {child.order}
                    </td>

                    <td className="p-3 border">

                        {child.is_menu
                            ? "Yes"
                            : "No"}

                    </td>

                    <td className="p-3 border">

                        {child.is_active
                            ? "Active"
                            : "Inactive"}

                    </td>

                    <td className="p-3 border">

                        <div className="flex gap-2">

                            <Link
                                to={`/dashboard/modules/edit/${child.id}`}
                                className="
                                    bg-yellow-500
                                    hover:bg-yellow-600
                                    text-white
                                    px-3
                                    py-1
                                    rounded
                                "
                            >
                                Edit
                            </Link>

                            <button
                                onClick={() =>
                                    handleDelete(child.id)
                                }
                                className="
                                    bg-red-600
                                    hover:bg-red-700
                                    text-white
                                    px-3
                                    py-1
                                    rounded
                                "
                            >
                                Delete
                            </button>

                        </div>

                    </td>

                </tr>

                {
                    child.children?.length > 0 &&
                    renderChildren(
                        child.children,
                        level + 1
                    )
                }

            </React.Fragment>
        ));
    };

    return (

        <div className="p-6">

            {/* HEADER */}

            <div className="flex justify-between items-center mb-6">

                <h1 className="text-2xl font-bold">

                    Modules

                </h1>

                <Link
                    to="/dashboard/modules/add"
                    className="
                        bg-blue-600
                        hover:bg-blue-700
                        text-white
                        px-4
                        py-2
                        rounded-lg
                    "
                >

                    Add Module

                </Link>

            </div>

            {/* TABLE */}

            <div className="overflow-x-auto bg-white rounded-xl shadow">

                <table className="w-full border-collapse">

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
                                Path
                            </th>

                            <th className="p-3 border">
                                Icon
                            </th>

                            <th className="p-3 border">
                                Order
                            </th>

                            <th className="p-3 border">
                                Menu
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

                        {
                            modules.map((module) => (

                                <React.Fragment key={module.id}>

                                    {/* MAIN MODULE */}

                                    <tr
                                        className="
                                            bg-gray-50
                                            hover:bg-gray-100
                                            font-semibold
                                        "
                                    >

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
                                            {module.path || "-"}
                                        </td>

                                        <td className="p-3 border">
                                            {module.icon || "-"}
                                        </td>

                                        <td className="p-3 border">
                                            {module.order}
                                        </td>

                                        <td className="p-3 border">

                                            {module.is_menu
                                                ? "Yes"
                                                : "No"}

                                        </td>

                                        <td className="p-3 border">

                                            {module.is_active
                                                ? "Active"
                                                : "Inactive"}

                                        </td>

                                        <td className="p-3 border">

                                            <div className="flex gap-2">

                                                <Link
                                                    to={`/dashboard/modules/edit/${module.id}`}
                                                    className="
                                                        bg-yellow-500
                                                        hover:bg-yellow-600
                                                        text-white
                                                        px-3
                                                        py-1
                                                        rounded
                                                    "
                                                >
                                                    Edit
                                                </Link>

                                                <button
                                                    onClick={() =>
                                                        handleDelete(module.id)
                                                    }
                                                    className="
                                                        bg-red-600
                                                        hover:bg-red-700
                                                        text-white
                                                        px-3
                                                        py-1
                                                        rounded
                                                    "
                                                >
                                                    Delete
                                                </button>

                                            </div>

                                        </td>

                                    </tr>

                                    {/* CHILD MODULES */}

                                    {
                                        module.children?.length > 0 &&
                                        renderChildren(
                                            module.children
                                        )
                                    }

                                </React.Fragment>
                            ))
                        }

                    </tbody>

                </table>

            </div>

        </div>
    );
}