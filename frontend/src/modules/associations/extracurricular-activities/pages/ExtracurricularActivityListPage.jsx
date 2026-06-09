import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
} from "react-router-dom";

import toast from "react-hot-toast";

import CrudHeader from "@/modules/shared/components/crud/CrudHeader";
import DataTable from "@/modules/shared/components/crud/DataTable";
import Pagination from "@/modules/shared/components/crud/Pagination";
import ActionButtons from "@/modules/shared/components/crud/ActionButtons";
import ConfirmModal from "@/modules/shared/components/dialogs/ConfirmModal";

import extracurricularActivityService from "../services/extracurricularActivityService";

const ExtracurricularActivityListPage = () => {

    const navigate =
        useNavigate();

    const [activities, setActivities] =
        useState([]);

    const [loading, setLoading] =
        useState(true);

    const [currentPage, setCurrentPage] =
        useState(1);

    const [selectedId, setSelectedId] =
        useState(null);

    const [isModalOpen, setIsModalOpen] =
        useState(false);

    const itemsPerPage = 20;

    const fetchActivities = async () => {

        try {

            setLoading(true);

            const response =
                await extracurricularActivityService.getAll();

            setActivities(
                response?.data ||
                response ||
                []
            );

        } catch (error) {

            console.error(error);

            toast.error(
                "Failed to load activities"
            );

        } finally {

            setLoading(false);

        }
    };

    useEffect(() => {

        fetchActivities();

    }, []);

    const handleDelete = async (id) => {

        try {

            await extracurricularActivityService.delete(id);

            toast.success(
                "Activity deleted successfully"
            );

            fetchActivities();

        } catch (error) {

            console.error(error);

            toast.error(
                "Delete failed"
            );
        }
    };

    const columns = [

        {
            key: "name",
            label: "Activity",
        },

        {
            key: "category",
            label: "Category",
        },

        {
            key: "status",
            label: "Status",
        },

        {
            key: "start_date",
            label: "Start Date",
        },

        {
            key: "actions",
            label: "Actions",
        },
    ];

    const totalPages =
        Math.ceil(
            activities.length /
            itemsPerPage
        );

    const paginatedData =
        activities.slice(

            (currentPage - 1)
            * itemsPerPage,

            currentPage
            * itemsPerPage
        );

    const tableData =
        paginatedData.map(
            (activity) => ({

                ...activity,

                actions: (

                    <ActionButtons

                        onEdit={() =>
                            navigate(
                                `/dashboard/associations/extracurricular-activities/edit/${activity.id}`
                            )
                        }

                        onDelete={() => {

                            setSelectedId(
                                activity.id
                            );

                            setIsModalOpen(
                                true
                            );
                        }}

                    />
                ),
            })
        );

    if (loading) {

        return (
            <div className="p-6">
                Loading...
            </div>
        );
    }

    return (

        <div className="space-y-6">

            <CrudHeader

                title="Extracurricular Activities"

                description="Manage extracurricular activities"

                addLabel="Add Activity"

                onAdd={() =>
                    navigate(
                        "/dashboard/associations/extracurricular-activities/add"
                    )
                }

            />

            <DataTable

                columns={columns}

                data={tableData}

                currentPage={currentPage}

                itemsPerPage={itemsPerPage}

            />

            <Pagination

                currentPage={currentPage}

                totalPages={totalPages}

                onPageChange={setCurrentPage}

            />

            <ConfirmModal

                isOpen={isModalOpen}

                title="Delete Activity"

                message="Are you sure you want to delete this activity?"

                onCancel={() =>
                    setIsModalOpen(false)
                }

                onConfirm={() => {

                    handleDelete(
                        selectedId
                    );

                    setIsModalOpen(
                        false
                    );

                }}

            />

        </div>
    );
};

export default ExtracurricularActivityListPage;