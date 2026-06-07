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

import driverService from "../services/driverService";


const List = () => {

    // ======================
    // NAVIGATION
    // ======================

    const navigate = useNavigate();

    // ======================
    // STATES
    // ======================

    const [drivers, setDrivers] =
        useState([]);

    const [loading, setLoading] =
        useState(true);

    const [search, setSearch] =
        useState("");

    const [currentPage, setCurrentPage] =
        useState(1);

    const [deleteModal, setDeleteModal] =
        useState(false);

    const [selectedDriverId,
        setSelectedDriverId] =
        useState(null);

    // ======================
    // PAGINATION
    // ======================

    const itemsPerPage = 10;

    // ======================
    // FETCH DRIVERS
    // ======================

    const fetchDrivers = async () => {

        try {

            setLoading(true);

            const response =
                await driverService.getDrivers();

            const driversData =

                Array.isArray(response)

                    ? response

                    : response.results || [];

            setDrivers(driversData);

        } catch (error) {

            toast.error(
                "Failed to load drivers"
            );

        } finally {

            setLoading(false);
        }
    };

    // ======================
    // LOAD DRIVERS
    // ======================

    useEffect(() => {

        fetchDrivers();

    }, []);

    // ======================
    // DELETE DRIVER
    // ======================

    const handleDelete = async () => {

        try {

            await driverService.deleteDriver(
                selectedDriverId
            );

            toast.success(
                "Driver deleted successfully"
            );

            fetchDrivers();

        } catch (error) {

            toast.error(
                "Failed to delete driver"
            );

        } finally {

            setDeleteModal(false);
        }
    };

    // ======================
    // FILTER DRIVERS
    // ======================

    const filteredDrivers =
        drivers.filter((driver) =>

            driver.full_name
                ?.toLowerCase()
                .includes(
                    search.toLowerCase()
                )
        );

    // ======================
    // PAGINATION
    // ======================

    const totalPages = Math.ceil(

        filteredDrivers.length /
        itemsPerPage
    );

    const startIndex =

        (currentPage - 1) *
        itemsPerPage;

    const paginatedDrivers =
        filteredDrivers.slice(
            startIndex,
            startIndex + itemsPerPage
        );

    // ======================
    // TABLE COLUMNS
    // ======================

    const columns = [

        {
            key: "full_name",
            label: "Driver Name",
        },

        {
            key: "phone",
            label: "Phone",
        },

        {
            key: "license_number",
            label: "License Number",
        },

        {
            key: "license_expiry",
            label: "License Expiry",
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
        paginatedDrivers.map((driver) => ({

            ...driver,

            actions: (

                <ActionButtons

                    onView={() =>
                        navigate(
                            `/dashboard/transport/drivers/profile/${driver.id}`
                        )
                    }

                    onEdit={() =>
                        navigate(
                            `/dashboard/transport/drivers/edit/${driver.id}`
                        )
                    }

                    onDelete={() => {

                        setSelectedDriverId(
                            driver.id
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
                Loading drivers...
            </div>
        );
    }

    return (

        <div className="space-y-6">

            <CrudHeader
                title="Drivers"
                description="Manage transport drivers"
                addLabel="Add Driver"
                onAdd={() =>
                    navigate(
                        "/dashboard/transport/drivers/create"
                    )
                }
            />

            <SearchBox
                placeholder="Search drivers..."
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
                title="Delete Driver"
                message="Are you sure you want to delete this driver?"
                onCancel={() =>
                    setDeleteModal(false)
                }
                onConfirm={handleDelete}
            />

        </div>
    );
};

export default List;