import CrudListPage from "@/modules/shared/components/crud/CrudListPage";

const PrincipalsListPage = () => {

    const columns = [

        {
            key: "id",
            label: "ID",
        },

        {
            key: "school_name",
            label: "School",
        },

        {
            key: "name",
            label: "Name",
        },

        {
            key: "qualification",
            label: "Qualification",
        },

        {
            key: "joining_date",
            label: "Joining Date",
        },

    ];

    return (

        <CrudListPage
            title="Principals"
            endpoint="/schools/principals/"
            columns={columns}
            addPath="/dashboard/schools/principals/add"
            editPath="/dashboard/schools/principals/edit"
        />

    );

};

export default PrincipalsListPage;