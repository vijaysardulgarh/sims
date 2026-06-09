import CrudCreatePage from '../../../shared/components/crud/CrudCreatePage';

import CommunicationTemplateForm from '../components/CommunicationTemplateForm';

const AddCommunicationTemplatePage = () => {

    return (
        <CrudCreatePage
            title="Add Communication Template"
            endpoint="/communications/communication-templates/"
            FormComponent={CommunicationTemplateForm}
            redirectPath="/dashboard/communications/communication-templates"
        />
    );
};

export default AddCommunicationTemplatePage;