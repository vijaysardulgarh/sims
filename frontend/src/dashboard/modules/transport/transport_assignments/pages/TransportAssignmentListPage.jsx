import {
    useEffect,
    useState,
} from "react";

import { useNavigate } from "react-router-dom";

import toast from "react-hot-toast";

import CrudHeader from "@/dashboard/shared/components/crud/CrudHeader";

import DataTable from "@/dashboard/shared/components/crud/DataTable";

import SearchBox from "@/dashboard/shared/components/crud/SearchBox";

import Pagination from "@/dashboard/shared/components/crud/Pagination";

import ActionButtons from "@/dashboard/shared/components/crud/ActionButtons";

import DeleteModal from "@/dashboard/shared/components/crud/DeleteModal";

import transportAssignmentService from "../services/transportAssignmentService";


const List = () => {

    const navigate = useNavigate();

    const [assignments, setAssignments] =
        useState([]);

    const [loading, setLoading] =
        useState(true);

    const [search, setSearch] =
        useState("");

    const [currentPage, setCurrentPage] =
        useState(1);

    const [deleteModal, setDeleteModal] =
        useState(false);

    const [selectedAssignmentId,
        setSelectedAssignmentId] =
        useState(null);

    const itemsPerPage = 10;

    const fetchAssignments = async () => {

        try {

            setLoading(true);

            const response =
                await transportAssignmentService.getAssignments();

            const assignmentsData =

                Array.isArray(response)

                    ? response

                    : response.results || [];

            setAssignments(assignmentsData);

        } catch (error) {

            toast.error(
                "Failed to load assignments"
            );

        } finally {

            setLoading(false);
        }
    };

    useEffect(() => {

        fetchAssignments();

    }, []);

    const handleDelete = async () => {

        try {

            await transportAssignmentService.deleteAssignment(
                selectedAssignmentId
            );

            toast.success(
                "Assignment deleted successfully"
            );

            fetchAssignments();

        } catch (error) {

            toast.error(
                "Failed to delete assignment"
            );

        } finally {

            setDeleteModal(false);
        }
    };

    const filteredAssignments =
        assignments.filter((assignment) =>

            assignment.student_name
                ?.toLowerCase()
                .includes(
                    search.toLowerCase()
                )
        );

    const totalPages = Math.ceil(

        filteredAssignments.length /
        itemsPerPage
    );

    const startIndex =

        (currentPage - 1) *
        itemsPerPage;

    const paginatedAssignments =
        filteredAssignments.slice(
            startIndex,
            startIndex + itemsPerPage
        );

    const columns = [

        {
            key: "student_name",
            label: "Student Name",
        },

        {
            key: "pickup_point",
            label: "Pickup Point",
        },

        {
            key: "monthly_fee",
            label: "Monthly Fee",
        },

        {
            key: "actions",
            label: "Actions",
        },
    ];

    const tableData =
        paginatedAssignments.map((assignment) => ({

            ...assignment,

            actions: (

                <ActionButtons

                    onView={() =>
                        navigate(
                            `/dashboard/transport/transport-assignments/profile/${assignment.id}`
                        )
                    }

                    onEdit={() =>
                        navigate(
                            `/dashboard/transport/transport-assignments/edit/${assignment.id}`
                        )
                    }

                    onDelete={() => {

                        setSelectedAssignmentId(
                            assignment.id
                        );

                        setDeleteModal(true);
                    }}
                />
            ),
        }));

    if (loading) {

        return (
            <div>
                Loading assignments...
            </div>
        );
    }

    return (

        <div className="space-y-6">

            <CrudHeader
                title="Transport Assignments"
                description="Manage student transport assignments"
                addLabel="Add Assignment"
                onAdd={() =>
                    navigate(
                        "/dashboard/transport/transport-assignments/create"
                    )
                }
            />

            <SearchBox
                placeholder="Search assignments..."
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
                title="Delete Assignment"
                message="Are you sure you want to delete this assignment?"
                onCancel={() =>
                    setDeleteModal(false)
                }
                onConfirm={handleDelete}
            />

        </div>
    );
};

export default List;