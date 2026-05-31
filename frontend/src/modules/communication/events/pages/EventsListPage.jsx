import CrudListPage from '../../../../shared/components/crud/CrudListPage';

const EventsListPage = () => {

    const columns = [

        {
            key: 'title',
            label: 'Title',
        },

        {
            key: 'event_date',
            label: 'Date',
        },

        {
            key: 'venue',
            label: 'Venue',
        },

        {
            key: 'organizer',
            label: 'Organizer',
        },

        {
            key: 'is_active',
            label: 'Active',
        },
    ];

    return (
        <CrudListPage
            title="Events"
            endpoint="/communications/events/"
            columns={columns}
            addPath="/dashboard/communications/events/add"
            editPath="/dashboard/communications/events/edit"
        />
    );
};

export default EventsListPage;