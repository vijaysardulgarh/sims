import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

import api from "../../../../services/api/axios";

import DataTable from "@/modules/shared/components/crud/DataTable";
import ConfirmModal from "@/modules/shared/components/dialogs/ConfirmModal";
import ActionButtons from "@/modules/shared/components/crud/ActionButtons";
import CrudHeader from "@/modules/shared/components/crud/CrudHeader";

const AcademicSessionsListPage = () => {
    const navigate = useNavigate();

    const [sessions, setSessions] = useState([]);
    const [loading, setLoading] = useState(true);

    const [deleteId, setDeleteId] = useState(null);
    const [isModalOpen, setIsModalOpen] = useState(false);

    // ==========================================
    // FETCH SESSIONS
    // ==========================================

    const fetchSessions = async () => {
        try {
            setLoading(true);

            const response = await api.get("/academics/sessions/");

            setSessions(
                response.data.results ||
                response.data ||
                []
            );
        } catch (error) {
            console.error(error);
            toast.error("Failed to load academic sessions.");
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchSessions();
    }, []);

    // ==========================================
    // DELETE
    // ==========================================

    const handleDelete = async (id) => {
        try {
            await api.delete(`/academics/sessions/${id}/`);

            toast.success("Academic session deleted successfully.");

            fetchSessions();
        } catch (error) {
            console.error(error);
            toast.error("Failed to delete session.");
        }
    };

    // ==========================================
    // TABLE COLUMNS
    // ==========================================

    const columns = [
        {
            key: "name",
            label: "Session",
        },
        {
            key: "start_date",
            label: "Start Date",
        },
        {
            key: "end_date",
            label: "End Date",
        },
        {
            key: "is_current",
            label: "Current",
        },
        {
            key: "actions",
            label: "Actions",
        },
    ];

    // ==========================================
    // TABLE DATA
    // ==========================================

    const tableData = sessions.map((session) => ({
        ...session,

        is_current: session.is_current ? (
            <span
                className="
                    inline-flex
                    items-center
                    rounded-full
                    bg-green-100
                    px-3
                    py-1
                    text-xs
                    font-semibold
                    text-green-700
                "
            >
                ✓ Current
            </span>
        ) : (
            <span
                className="
                    inline-flex
                    items-center
                    rounded-full
                    bg-gray-100
                    px-3
                    py-1
                    text-xs
                    font-semibold
                    text-gray-600
                "
            >
                Previous
            </span>
        ),

        actions: (
            <ActionButtons
                onEdit={() =>
                    navigate(
                        `/dashboard/academics/sessions/edit/${session.id}`
                    )
                }
                onDelete={() => {
                    setDeleteId(session.id);
                    setIsModalOpen(true);
                }}
            />
        ),
    }));

    if (loading) {
        return (
            <div className="p-6 text-center text-gray-500">
                Loading academic sessions...
            </div>
        );
    }

    return (
        <div className="space-y-6">
            <CrudHeader
                title="Academic Sessions"
                description="Manage academic sessions"
                addLabel="Add Session"
                onAdd={() =>
                    navigate("/dashboard/academics/sessions/add")
                }
            />

            <div
                className="
                    bg-white
                    rounded-2xl
                    border
                    shadow-sm
                    overflow-hidden
                "
            >
                <DataTable
                    columns={columns}
                    data={tableData}
                />
            </div>

            <ConfirmModal
                isOpen={isModalOpen}
                title="Delete Academic Session"
                message="Are you sure you want to delete this academic session?"
                onCancel={() => setIsModalOpen(false)}
                onConfirm={() => {
                    handleDelete(deleteId);
                    setIsModalOpen(false);
                }}
            />
        </div>
    );
};

export default AcademicSessionsListPage;