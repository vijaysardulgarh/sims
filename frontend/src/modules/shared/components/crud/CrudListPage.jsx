import {
    useEffect,
    useState
} from "react";

import {
    Link
} from "react-router-dom";

import api from "../../../../services/api/axios";

const CrudListPage = ({
    title,
    endpoint,
    columns,
    addPath,
    editPath,
}) => {

    const [rows, setRows] =
        useState([]);

    const [loading, setLoading] =
        useState(true);

    useEffect(() => {

        loadData();

    }, []);

    const loadData = async () => {

        try {

            const response =
                await api.get(
                    endpoint
                );

            const data =

                response?.data?.results ||

                response?.data?.data ||

                response?.data ||

                [];

            setRows(data);

        }

        catch (error) {

            console.error(error);

        }

        finally {

            setLoading(false);

        }

    };

    const handleDelete = async (
        id
    ) => {

        const confirmed =
            window.confirm(
                "Delete record?"
            );

        if (!confirmed) return;

        try {

            await api.delete(
                `${endpoint}${id}/`
            );

            loadData();

        }

        catch (error) {

            console.error(error);

        }

    };

    return (

        <div className="space-y-6">

            {/* HEADER */}

            <div
                className="
                    flex
                    items-center
                    justify-between
                "
            >

                <div>

                    <h1
                        className="
                            text-3xl
                            font-bold
                            text-gray-900
                        "
                    >
                        {title}
                    </h1>

                    <p
                        className="
                            text-gray-500
                            mt-1
                        "
                    >
                        Manage {title.toLowerCase()}
                    </p>

                </div>

                <Link

                    to={addPath}

                    className="
                        px-5
                        py-3
                        bg-blue-600
                        text-white
                        rounded-xl
                        font-medium
                        hover:bg-blue-700
                        transition
                    "
                >

                    Add

                </Link>

            </div>

            {/* TABLE */}

            <div
                className="
                    bg-white
                    rounded-2xl
                    shadow
                    overflow-hidden
                "
            >

                {

                    loading ? (

                        <div
                            className="
                                p-10
                                text-center
                                text-gray-500
                            "
                        >

                            Loading...

                        </div>

                    ) : (

                        <div
                            className="
                                overflow-x-auto
                            "
                        >

                            <table
                                className="
                                    min-w-full
                                "
                            >

                                <thead
                                    className="
                                        bg-gray-100
                                    "
                                >

                                    <tr>

                                        {

                                            columns.map(
                                                (
                                                    column
                                                ) => (

                                                    <th

                                                        key={
                                                            column.key
                                                        }

                                                        className="
                                                            px-6
                                                            py-4
                                                            text-left
                                                            text-sm
                                                            font-semibold
                                                            text-gray-700
                                                        "
                                                    >

                                                        {
                                                            column.label
                                                        }

                                                    </th>

                                                )
                                            )

                                        }

                                        <th
                                            className="
                                                px-6
                                                py-4
                                                text-left
                                                text-sm
                                                font-semibold
                                                text-gray-700
                                            "
                                        >

                                            Actions

                                        </th>

                                    </tr>

                                </thead>

                                <tbody>

                                    {

                                        rows.length >

                                        0 ? (

                                            rows.map(
                                                (
                                                    row
                                                ) => (

                                                    <tr

                                                        key={
                                                            row.id
                                                        }

                                                        className="
                                                            border-b
                                                            hover:bg-gray-50
                                                        "
                                                    >

                                                        {

                                                            columns.map(
                                                                (
                                                                    column
                                                                ) => (

                                                                    <td

                                                                        key={
                                                                            column.key
                                                                        }

                                                                        className="
                                                                            px-6
                                                                            py-4
                                                                            text-sm
                                                                            text-gray-700
                                                                        "
                                                                    >

                                                                        {

                                                                            String(
                                                                                row[
                                                                                    column.key
                                                                                ] ??
                                                                                ""
                                                                            )

                                                                        }

                                                                    </td>

                                                                )
                                                            )

                                                        }

                                                        <td
                                                            className="
                                                                px-6
                                                                py-4
                                                                space-x-2
                                                            "
                                                        >

                                                            <Link

                                                                to={`${editPath}/${row.id}`}

                                                                className="
                                                                    inline-flex
                                                                    px-3
                                                                    py-2
                                                                    text-sm
                                                                    rounded-lg
                                                                    bg-yellow-500
                                                                    text-white
                                                                    hover:bg-yellow-600
                                                                "
                                                            >

                                                                Edit

                                                            </Link>

                                                            <button

                                                                className="
                                                                    inline-flex
                                                                    px-3
                                                                    py-2
                                                                    text-sm
                                                                    rounded-lg
                                                                    bg-red-600
                                                                    text-white
                                                                    hover:bg-red-700
                                                                "

                                                                onClick={() =>
                                                                    handleDelete(
                                                                        row.id
                                                                    )
                                                                }
                                                            >

                                                                Delete

                                                            </button>

                                                        </td>

                                                    </tr>

                                                )
                                            )

                                        ) : (

                                            <tr>

                                                <td

                                                    colSpan={
                                                        columns.length + 1
                                                    }

                                                    className="
                                                        py-10
                                                        text-center
                                                        text-gray-500
                                                    "
                                                >

                                                    No records found

                                                </td>

                                            </tr>

                                        )

                                    }

                                </tbody>

                            </table>

                        </div>

                    )

                }

            </div>

        </div>

    );

};

export default CrudListPage;