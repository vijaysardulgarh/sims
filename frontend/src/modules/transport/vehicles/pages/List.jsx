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

import vehicleService from "../services/Service";


const List = () => {

    // ======================
    // NAVIGATION
    // ======================

    const navigate = useNavigate();

    // ======================
    // STATES
    // ======================

    const [vehicles, setVehicles] =
        useState([]);

    const [loading, setLoading] =
        useState(true);

    const [search, setSearch] =
        useState("");

    const [currentPage, setCurrentPage] =
        useState(1);

    const [deleteModal, setDeleteModal] =
        useState(false);

    const [selectedVehicleId,
        setSelectedVehicleId] =
        useState(null);

    // ======================
    // PAGINATION
    // ======================

    const itemsPerPage = 10;

    // ======================
    // FETCH VEHICLES
    // ======================

    const fetchVehicles = async () => {

        try {

            setLoading(true);

            const response =
                await vehicleService.getVehicles();

            const vehiclesData =

                Array.isArray(response)

                    ? response

                    : response.results || [];

            setVehicles(vehiclesData);

        } catch (error) {

            toast.error(
                "Failed to load vehicles"
            );

        } finally {

            setLoading(false);
        }
    };

    // ======================
    // LOAD DATA
    // ======================

    useEffect(() => {

        fetchVehicles();

    }, []);

    // ======================
    // DELETE VEHICLE
    // ======================

    const handleDelete = async () => {

        try {

            await vehicleService.deleteVehicle(
                selectedVehicleId
            );

            toast.success(
                "Vehicle deleted successfully"
            );

            fetchVehicles();

        } catch (error) {

            toast.error(
                "Failed to delete vehicle"
            );

        } finally {

            setDeleteModal(false);
        }
    };

    // ======================
    // FILTER VEHICLES
    // ======================

    const filteredVehicles =
        vehicles.filter((vehicle) =>

            vehicle.vehicle_number
                ?.toLowerCase()
                .includes(
                    search.toLowerCase()
                )
        );

    // ======================
    // PAGINATION
    // ======================

    const totalPages = Math.ceil(

        filteredVehicles.length /
        itemsPerPage
    );

    const startIndex =

        (currentPage - 1) *
        itemsPerPage;

    const paginatedVehicles =
        filteredVehicles.slice(
            startIndex,
            startIndex + itemsPerPage
        );

    // ======================
    // TABLE COLUMNS
    // ======================

    const columns = [

        {
            key: "vehicle_number",
            label: "Vehicle Number",
        },

        {
            key: "vehicle_type",
            label: "Vehicle Type",
        },

        {
            key: "registration_number",
            label: "Registration Number",
        },

        {
            key: "capacity",
            label: "Capacity",
        },

        {
            key: "actions",
            label: "Actions",
        },
    ];

    // ======================
    // TABLE DATA
    // ======================

    const tableData =
        paginatedVehicles.map((vehicle) => ({

            ...vehicle,

            actions: (

                <ActionButtons

                    onView={() =>
                        navigate(
                            `/dashboard/transport/vehicles/profile/${vehicle.id}`
                        )
                    }

                    onEdit={() =>
                        navigate(
                            `/dashboard/transport/vehicles/edit/${vehicle.id}`
                        )
                    }

                    onDelete={() => {

                        setSelectedVehicleId(
                            vehicle.id
                        );

                        setDeleteModal(true);
                    }}
                />
            ),
        }));

    // ======================
    // LOADING UI
    // ======================

    if (loading) {

        return (
            <div>
                Loading vehicles...
            </div>
        );
    }

    return (

        <div className="space-y-6">

            <CrudHeader
                title="Vehicles"
                description="Manage transport vehicles"
                addLabel="Add Vehicle"
                onAdd={() =>
                    navigate(
                        "/dashboard/transport/vehicles/create"
                    )
                }
            />

            <SearchBox
                placeholder="Search vehicles..."
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
                title="Delete Vehicle"
                message="Are you sure you want to delete this vehicle?"
                onCancel={() =>
                    setDeleteModal(false)
                }
                onConfirm={handleDelete}
            />

        </div>
    );
};

export default List;