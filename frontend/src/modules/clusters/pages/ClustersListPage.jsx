// src/modules/clusters/pages/ClustersListPage.jsx

import CrudListPage from "@/modules/shared/components/crud/CrudListPage";

const ClustersListPage = () => {

    const columns = [

        {
            key: "name",
            label: "Cluster Name",
        },

        {
            key: "code",
            label: "Code",
        },

        {
            key: "crc_name",
            label: "CRC Name",
        },

        {
            key: "crc_phone",
            label: "CRC Phone",
        },

        {
            key: "email",
            label: "Office Email",
        },

        {
            key: "phone",
            label: "Office Phone",
        },

        {
            key: "is_active",
            label: "Status",
            render: (row) => (
                <span
                    className={
                        row.is_active
                            ? "text-green-600 font-medium"
                            : "text-red-600 font-medium"
                    }
                >
                    {row.is_active ? "Active" : "Inactive"}
                </span>
            ),
        },

    ];

    return (

        <CrudListPage

            title="Clusters"

            description="Manage school clusters"

            endpoint="/clusters/"

            columns={columns}

            addLabel="Add Cluster"

            addPath="/dashboard/clusters/create"

            editPath="/dashboard/clusters/edit"

        />

    );

};

export default ClustersListPage;