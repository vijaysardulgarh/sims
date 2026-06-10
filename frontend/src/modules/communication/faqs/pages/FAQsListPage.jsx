import CrudListPage
    from "../../../shared/components/crud/CrudListPage";

const FAQsListPage = () => {

    const columns = [

        {
            label: "Question",
            key: "question",
        },

        {
            label: "Category",
            key: "category",
        },

        {
            label: "Order",
            key: "order",
        },

    ];

    return (

        <CrudListPage
            title="FAQs"
            endpoint="/communications/faqs/"
            columns={columns}
            addPath="/dashboard/communications/faqs/add"
            editPath="/dashboard/communications/faqs/edit"
        />

    );

};

export default FAQsListPage;