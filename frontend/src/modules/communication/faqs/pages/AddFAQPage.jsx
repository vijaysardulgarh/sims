import FAQForm from "../components/FAQForm";

import CrudCreatePage
    from "../../../shared/components/crud/CrudCreatePage";

const AddFAQPage = () => {

    return (
        <CrudCreatePage
            title="Add FAQ"
            endpoint="/communications/faqs/"
            FormComponent={FAQForm}
            redirectPath="/dashboard/communications/faqs"
            successMessage="FAQ created successfully."
        />
    );
};

export default AddFAQPage;