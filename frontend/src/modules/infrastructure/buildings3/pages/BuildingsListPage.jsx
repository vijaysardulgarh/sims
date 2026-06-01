import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
} from "react-router-dom";

import Button
from "../../../../components/ui/Button";

import CrudPage
from "../../../../components/crud/CrudPage";

import buildingColumns
from "../config/buildingColumns";

import {
    getBuildings,
    deleteBuilding,
} from "../services/buildingService";

const BuildingsListPage = () => {

    const navigate =
        useNavigate();

    const [search, setSearch] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    const [page, setPage] =
        useState(1);

    const [buildings,
        setBuildings] =
        useState([]);

    useEffect(() => {

        loadBuildings();

    }, []);

    const loadBuildings =
        async () => {

            try {

                setLoading(true);

                const response =
                    await getBuildings();

                setBuildings(
                    response.data
                );

            } catch (error) {

                console.error(error);

            } finally {

                setLoading(false);

            }

        };

    const handleDelete =
        async (row) => {

            const confirmed =
                window.confirm(
                    `Delete ${row.name}?`
                );

            if (!confirmed)
                return;

            try {

                await deleteBuilding(
                    row.id
                );

                loadBuildings();

            } catch (error) {

                console.error(error);

            }

        };

    const filteredData =
        buildings.filter(
            (building) =>
                building.name
                    ?.toLowerCase()
                    .includes(
                        search.toLowerCase()
                    ) ||
                building.code
                    ?.toLowerCase()
                    .includes(
                        search.toLowerCase()
                    )
        );

    return (

        <CrudPage

            title="Buildings"

            subtitle="Manage school buildings"

            breadcrumbs={[

                "Dashboard",

                "Infrastructure",

                "Buildings",

            ]}

            search={search}

            onSearch={setSearch}

            columns={
                buildingColumns
            }

            data={
                filteredData
            }

            loading={loading}

            currentPage={page}

            totalPages={1}

            onPageChange={
                setPage
            }

            selectedCount={0}

            onBulkDelete={() => {}}

            onView={(row) =>
                console.log(row)
            }

            onEdit={(row) =>
                navigate(
                    `/dashboard/buildings/${row.id}/edit`
                )
            }

            onDelete={
                handleDelete
            }

            headerActions={

                <Button
                    onClick={() =>
                        navigate(
                            "/dashboard/buildings/add"
                        )
                    }
                >
                    Add Building
                </Button>

            }

        />

    );

};

export default BuildingsListPage;