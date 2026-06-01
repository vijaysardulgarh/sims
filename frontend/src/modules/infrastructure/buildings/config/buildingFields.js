const buildingFields = [
    {
        name: "building_name",
        label: "Building Name",
        type: "text",
    },
    {
        name: "building_code",
        label: "Building Code",
        type: "text",
    },
    {
        name: "status",
        label: "Status",
        type: "select",
        options: [
            {
                value: "active",
                label: "Active",
            },
            {
                value: "inactive",
                label: "Inactive",
            },
        ],
    },
];

export default buildingFields;