import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
} from "react-router-dom";

import toast from "react-hot-toast";

import schoolService from "../services/schoolService";

import CrudHeader from "@/modules/shared/components/crud/CrudHeader";
import DataTable from "@/modules/shared/components/crud/DataTable";
import Pagination from "@/modules/shared/components/crud/Pagination";
import ActionButtons from "@/modules/shared/components/crud/ActionButtons";
import ConfirmModal from "@/modules/shared/components/dialogs/ConfirmModal";

const SchoolsListPage = () => {

    const navigate = useNavigate();

    const [schools, setSchools] = useState([]);

    const [loading, setLoading] = useState(true);

    const [currentPage, setCurrentPage] = useState(1);

    const [selectedId, setSelectedId] = useState(null);

    const [isModalOpen, setIsModalOpen] = useState(false);

    const itemsPerPage = 20;

    useEffect(() => {

        fetchSchools();

    }, []);

    const fetchSchools = async () => {

        try {

            setLoading(true);

            const response =
                await schoolService.getSchools();

            setSchools(
                response?.data?.results ||
                response?.data ||
                []
            );

        }

        catch (error) {

            console.error(error);

            toast.error("Failed to load schools");

        }

        finally {

            setLoading(false);

        }

    };

    const handleDelete = async (id) => {

        try {

            await schoolService.deleteSchool(id);

            toast.success("School deleted successfully");

            fetchSchools();

        }

        catch (error) {

            console.error(error);

            toast.error("Delete failed");

        }

    };

    const totalPages = Math.ceil(
        schools.length / itemsPerPage
    );

    const paginatedSchools =
        schools.slice(
            (currentPage - 1) * itemsPerPage,
            currentPage * itemsPerPage
        );

    const columns = [

        {
            key: "name",
            label: "School Name",
        },

        {
            key: "code",
            label: "School Code",
        },

        {
            key: "email",
            label: "Email",
        },

        {
            key: "actions",
            label: "Actions",
        },

    ];

    const tableData = paginatedSchools.map(
        (school) => ({

            ...school,

            actions: (

                <ActionButtons

                    onEdit={() =>
                        navigate(
                            `/dashboard/schools/schools/edit/${school.id}`
                        )
                    }

                    onDelete={() => {

                        setSelectedId(school.id);

                        setIsModalOpen(true);

                    }}

                />

            ),

        })
    );

    if (loading) {

        return (
            <div className="p-6">
                Loading schools...
            </div>
        );

    }

    return (

        <div className="space-y-6 p-6">

            <CrudHeader

                title="Schools"

                description="Manage all schools"

                addLabel="Add School"

                onAdd={() =>
                    navigate(
                        "/dashboard/schools/schools/add"
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

                title="Delete School"

                message="Are you sure you want to delete this school?"

                onCancel={() =>
                    setIsModalOpen(false)
                }

                onConfirm={() => {

                    handleDelete(selectedId);

                    setIsModalOpen(false);

                }}

            />

        </div>

    );

};

export default SchoolsListPage;