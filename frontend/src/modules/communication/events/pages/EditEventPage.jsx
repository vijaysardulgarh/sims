import CrudEditPage from '../../../../shared/components/crud/CrudEditPage';

import EventForm from '../components/EventForm';

const EditEventPage = () => {

    return (
        <CrudEditPage
            title="Edit Event"
            endpoint="/communications/events/"
            FormComponent={EventForm}
            redirectPath="/dashboard/communications/events"
        />
    );
};

export default EditEventPage;