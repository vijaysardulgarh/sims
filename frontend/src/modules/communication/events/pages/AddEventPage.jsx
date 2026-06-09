import CrudCreatePage from '../../../shared/components/crud/CrudCreatePage';

import EventForm from '../components/EventForm';

const AddEventPage = () => {

    return (
        <CrudCreatePage
            title="Add Event"
            endpoint="/communications/events/"
            FormComponent={EventForm}
            redirectPath="/dashboard/communications/events"
        />
    );
};

export default AddEventPage;