import CrudListPage from "@/modules/shared/components/crud/CrudListPage";

const AboutSchoolListPage = () => {

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
            key: "history",
            label: "History",
        },
        {
            key: "vision",
            label: "Vision",
        },
        {
            key: "mission",
            label: "Mission",
        },
    ];

    return (
        <CrudListPage
            title="About Schools"
            endpoint="/schools/about-schools/"
            columns={columns}
            addPath="/dashboard/schools/about-schools/add"
            editPath="/dashboard/schools/about-schools/edit"
        />
    );
};

export default AboutSchoolListPage;