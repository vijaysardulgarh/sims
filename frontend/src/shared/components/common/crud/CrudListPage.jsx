import { useEffect, useState } from 'react';

import { Link } from 'react-router-dom';

import api from '../../../../services/api/axios';

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
                await api.get(endpoint);

            setRows(
                response.data.results ||
                response.data
            );

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);
        }
    };

    const handleDelete =
        async (id) => {

            const confirmed =
                window.confirm(
                    'Delete record?'
                );

            if (!confirmed) return;

            try {

                await api.delete(
                    `${endpoint}${id}/`
                );

                loadData();

            } catch (error) {

                console.error(error);
            }
        };

    return (
        <div className="container-fluid">

            <div
                className="
                    d-flex
                    justify-content-between
                    align-items-center
                    mb-3
                "
            >

                <h3>
                    {title}
                </h3>

                <Link
                    to={addPath}
                    className="
                        btn
                        btn-primary
                    "
                >
                    Add
                </Link>

            </div>

            {loading ? (

                <p>
                    Loading...
                </p>

            ) : (

                <table
                    className="
                        table
                        table-bordered
                    "
                >

                    <thead>

                        <tr>

                            {columns.map(
                                (column) => (

                                    <th
                                        key={
                                            column.key
                                        }
                                    >
                                        {
                                            column.label
                                        }
                                    </th>
                                )
                            )}

                            <th>
                                Actions
                            </th>

                        </tr>

                    </thead>

                    <tbody>

                        {rows.map(
                            (row) => (

                                <tr
                                    key={
                                        row.id
                                    }
                                >

                                    {columns.map(
                                        (
                                            column
                                        ) => (

                                            <td
                                                key={
                                                    column.key
                                                }
                                            >
                                                {
                                                    String(
                                                        row[
                                                            column.key
                                                        ]
                                                    )
                                                }
                                            </td>
                                        )
                                    )}

                                    <td>

                                        <Link
                                            to={`${editPath}/${row.id}`}
                                            className="
                                                btn
                                                btn-sm
                                                btn-warning
                                                me-2
                                            "
                                        >
                                            Edit
                                        </Link>

                                        <button
                                            className="
                                                btn
                                                btn-sm
                                                btn-danger
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
                        )}

                    </tbody>

                </table>
            )}

        </div>
    );
};

export default CrudListPage;