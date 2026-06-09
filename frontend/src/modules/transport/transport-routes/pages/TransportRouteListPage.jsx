import {
    useEffect,
    useState,
} from "react";

import { useNavigate } from "react-router-dom";

import toast from "react-hot-toast";

import CrudHeader from "@/modules/shared/components/crud/CrudHeader";

import DataTable from "@/modules/shared/components/crud/DataTable";

import SearchBox from "@/modules/shared/components/crud/SearchBox";

import Pagination from "@/modules/shared/components/crud/Pagination";

import ActionButtons from "@/modules/shared/components/crud/ActionButtons";

import DeleteModal from "@/dashboard/shared/components/crud/DeleteModal";

import transportRouteService from "../services/transportRouteService";


const List = () => {

    const navigate = useNavigate();

    const [routes, setRoutes] =
        useState([]);

    const [loading, setLoading] =
        useState(true);

    const [search, setSearch] =
        useState("");

    const [currentPage, setCurrentPage] =
        useState(1);

    const [deleteModal, setDeleteModal] =
        useState(false);

    const [selectedRouteId,
        setSelectedRouteId] =
        useState(null);

    const itemsPerPage = 10;

    const fetchRoutes = async () => {

        try {

            setLoading(true);

            const response =
                await transportRouteService.getRoutes();

            const routesData =

                Array.isArray(response)

                    ? response

                    : response.results || [];

            setRoutes(routesData);

        } catch (error) {

            toast.error(
                "Failed to load routes"
            );

        } finally {

            setLoading(false);
        }
    };

    useEffect(() => {

        fetchRoutes();

    }, []);

    const handleDelete = async () => {

        try {

            await transportRouteService.deleteRoute(
                selectedRouteId
            );

            toast.success(
                "Route deleted successfully"
            );

            fetchRoutes();

        } catch (error) {

            toast.error(
                "Failed to delete route"
            );

        } finally {

            setDeleteModal(false);
        }
    };

    const filteredRoutes =
        routes.filter((route) =>

            route.route_name
                ?.toLowerCase()
                .includes(
                    search.toLowerCase()
                )
        );

    const totalPages = Math.ceil(

        filteredRoutes.length /
        itemsPerPage
    );

    const startIndex =

        (currentPage - 1) *
        itemsPerPage;

    const paginatedRoutes =
        filteredRoutes.slice(
            startIndex,
            startIndex + itemsPerPage
        );

    const columns = [

        {
            key: "route_name",
            label: "Route Name",
        },

        {
            key: "start_location",
            label: "Start Location",
        },

        {
            key: "end_location",
            label: "End Location",
        },

        {
            key: "actions",
            label: "Actions",
        },
    ];

    const tableData =
        paginatedRoutes.map((route) => ({

            ...route,

            actions: (

                <ActionButtons

                    onView={() =>
                        navigate(
                            `/dashboard/transport/transport-routes/profile/${route.id}`
                        )
                    }

                    onEdit={() =>
                        navigate(
                            `/dashboard/transport/transport-routes/edit/${route.id}`
                        )
                    }

                    onDelete={() => {

                        setSelectedRouteId(
                            route.id
                        );

                        setDeleteModal(true);
                    }}
                />
            ),
        }));

    if (loading) {

        return (
            <div>
                Loading routes...
            </div>
        );
    }

    return (

        <div className="space-y-6">

            <CrudHeader
                title="Transport Routes"
                description="Manage transport routes"
                addLabel="Add Route"
                onAdd={() =>
                    navigate(
                        "/dashboard/transport/transport-routes/create"
                    )
                }
            />

            <SearchBox
                placeholder="Search routes..."
                value={search}
                onChange={(e) =>
                    setSearch(e.target.value)
                }
            />

            <DataTable
                columns={columns}
                data={tableData}
            />

            <Pagination
                currentPage={currentPage}
                totalPages={totalPages}
                onPageChange={setCurrentPage}
            />

            <DeleteModal
                isOpen={deleteModal}
                title="Delete Route"
                message="Are you sure you want to delete this route?"
                onCancel={() =>
                    setDeleteModal(false)
                }
                onConfirm={handleDelete}
            />

        </div>
    );
};

export default List;