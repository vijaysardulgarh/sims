import StatusBadge
from "../../../../components/ui/StatusBadge";

const buildingColumns = [

    {
        key: "name",
        label: "Building Name",
    },

    {
        key: "code",
        label: "Code",
    },

    {
        key: "number_of_floors",
        label: "Floors",
    },

    {
        key: "school_name",
        label: "School",
    },

    {
        key: "is_active",
        label: "Status",

        render: (row) => (

            <StatusBadge
                status={
                    row.is_active
                        ? "Active"
                        : "Inactive"
                }
            />

        ),
    },

];

export default buildingColumns;