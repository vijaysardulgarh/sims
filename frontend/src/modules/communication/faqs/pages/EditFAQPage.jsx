import FAQForm from "../components/FAQForm";

import CrudEditPage
    from "../../../shared/components/crud/CrudEditPage";

const EditFAQPage = () => {

    return (
        <CrudEditPage
            title="Edit FAQ"
            endpoint="/communications/faqs"
            FormComponent={FAQForm}
            redirectPath="/dashboard/communications/faqs"
            successMessage="FAQ updated successfully."
        />
    );
};

export default EditFAQPage;