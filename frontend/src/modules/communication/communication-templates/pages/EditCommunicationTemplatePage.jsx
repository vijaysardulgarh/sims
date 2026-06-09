import CrudEditPage from '../../../shared/components/crud/CrudEditPage';

import CommunicationTemplateForm from '../components/CommunicationTemplateForm';

const EditCommunicationTemplatePage = () => {

    return (
        <CrudEditPage
            title="Edit Communication Template"
            endpoint="/communications/communication-templates/"
            FormComponent={CommunicationTemplateForm}
            redirectPath="/dashboard/communications/communication-templates"
        />
    );
};

export default EditCommunicationTemplatePage;