// ============================================
// CLASSROOMS LIST
// File: ClassroomsList.jsx
// ============================================

import {
    useEffect,
    useState
} from "react";

import {
    useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import DataTable from "../../../../dashboard/shared/components/crud/DataTable";
import SearchBox from "../../../../dashboard/shared/components/crud/SearchBox";
import Pagination from "../../../../dashboard/shared/components/crud/Pagination";
import CrudHeader from "../../../../dashboard/shared/components/crud/CrudHeader";
import ActionButtons from "../../../../dashboard/shared/components/crud/ActionButtons";
import ConfirmModal from "../../../../dashboard/shared/components/modals/ConfirmModal";

import classroomService from "../services/classroomService";

const ClassroomsList = () => {

    const navigate =
        useNavigate();

    const [classrooms, setClassrooms] =
        useState([]);

    const [loading, setLoading] =
        useState(true);

    const [search, setSearch] =
        useState("");

    const [currentPage, setCurrentPage] =
        useState(1);

    const [isModalOpen, setIsModalOpen] =
        useState(false);

    const [
        selectedClassroomId,
        setSelectedClassroomId
    ] = useState(null);

    const itemsPerPage = 20;

    // ============================================
    // FETCH CLASSROOMS
    // ============================================

    const fetchClassrooms = async () => {

        try {

            setLoading(true);

            const response =
                await classroomService.getClassrooms();

            const classroomsData =

                Array.isArray(
                    response
                )

                    ? response

                    : response.results || [];

            setClassrooms(
                classroomsData
            );

        } catch (error) {

            console.error(
                error
            );

            toast.error(
                "Failed to load classrooms"
            );

        } finally {

            setLoading(false);
        }
    };

    useEffect(() => {

        fetchClassrooms();

    }, []);

    // ============================================
    // DELETE CLASSROOM
    // ============================================

    const handleDelete = async (
        id
    ) => {

        try {

            await classroomService.deleteClassroom(
                id
            );

            toast.success(
                "Classroom deleted successfully"
            );

            fetchClassrooms();

        } catch (error) {

            console.error(
                error
            );

            toast.error(
                "Delete failed"
            );
        }
    };

    // ============================================
    // FILTER DATA
    // ============================================

    const filteredClassrooms =
        classrooms.filter(

            (classroom) =>

                classroom.classroom_code
                    ?.toLowerCase()
                    .includes(
                        search.toLowerCase()
                    )

                ||

                classroom.room_name
                    ?.toLowerCase()
                    .includes(
                        search.toLowerCase()
                    )

                ||

                classroom.room_number
                    ?.toLowerCase()
                    .includes(
                        search.toLowerCase()
                    )

                ||

                classroom.floor_name
                    ?.toLowerCase()
                    .includes(
                        search.toLowerCase()
                    )
        );

    // ============================================
    // PAGINATION
    // ============================================

    const totalPages =
        Math.ceil(

            filteredClassrooms.length

            /

            itemsPerPage
        );

    const paginatedClassrooms =
        filteredClassrooms.slice(

            (
                currentPage - 1
            )

            *

            itemsPerPage,

            currentPage

            *

            itemsPerPage
        );

    // ============================================
    // TABLE COLUMNS
    // ============================================

    const columns = [

        {
            key: "classroom_code",
            label: "Code",
        },

        {
            key: "room_number",
            label: "Room No.",
        },

        {
            key: "room_name",
            label: "Room Name",
        },

        {
            key: "floor_name",
            label: "Floor",
        },

        {
            key: "capacity",
            label: "Capacity",
        },

        {
            key: "smart_classroom",
            label: "Smart",
        },

        {
            key: "air_conditioned",
            label: "AC",
        },

        {
            key: "internet_enabled",
            label: "Internet",
        },

        {
            key: "is_active",
            label: "Status",
        },

        {
            key: "actions",
            label: "Actions",
        },
    ];

    // ============================================
    // TABLE DATA
    // ============================================

    const tableData =
        paginatedClassrooms.map(

            (
                classroom
            ) => ({

                ...classroom,

                smart_classroom:

                    classroom.smart_classroom

                        ? "Yes"

                        : "No",

                air_conditioned:

                    classroom.air_conditioned

                        ? "Yes"

                        : "No",

                internet_enabled:

                    classroom.internet_enabled

                        ? "Yes"

                        : "No",

                is_active:

                    classroom.is_active

                        ? "Active"

                        : "Inactive",

                actions: (

                    <ActionButtons

                        onEdit={() =>

                            navigate(

                                `/dashboard/infrastructure/classrooms/${classroom.id}/edit`
                            )
                        }

                        onDelete={() => {

                            setSelectedClassroomId(
                                classroom.id
                            );

                            setIsModalOpen(
                                true
                            );
                        }}
                    />
                ),
            })
        );

    // ============================================
    // LOADING
    // ============================================

    if (loading) {

        return (

            <div className="p-6">

                Loading classrooms...

            </div>
        );
    }

    // ============================================
    // UI
    // ============================================

    return (

        <div className="space-y-6">

            <CrudHeader

                title="Classrooms"

                description="Manage classrooms"

                addLabel="Add Classroom"

                onAdd={() =>

                    navigate(

                        "/dashboard/infrastructure/classrooms/add"
                    )
                }
            />

            <SearchBox

                placeholder="Search classroom code, room, floor..."

                value={search}

                onChange={(e) =>

                    setSearch(
                        e.target.value
                    )
                }
            />

            <DataTable

                columns={columns}

                data={tableData}
            />

            <Pagination

                currentPage={
                    currentPage
                }

                totalPages={
                    totalPages
                }

                onPageChange={
                    setCurrentPage
                }
            />

            <ConfirmModal

                isOpen={
                    isModalOpen
                }

                title="Delete Classroom"

                message="Are you sure you want to delete this classroom?"

                onCancel={() =>

                    setIsModalOpen(
                        false
                    )
                }

                onConfirm={() => {

                    handleDelete(
                        selectedClassroomId
                    );

                    setIsModalOpen(
                        false
                    );
                }}
            />

        </div>
    );
};

export default ClassroomsList;