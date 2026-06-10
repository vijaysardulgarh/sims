import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

const AffiliationsListPage = () => {

    const columns = [

        {
            key: 'board',
            label: 'Board',
        },

        {
            key: 'affiliation_number',
            label: 'Affiliation No.',
        },

        {
            key: 'status',
            label: 'Status',
        },

        {
            key: 'valid_upto',
            label: 'Valid Upto',
        },

    ];

    return (

        <CrudListPage
            title="Affiliations"
            endpoint="/compliance/affiliations/"
            columns={columns}
            addPath="/dashboard/compliance/affiliations/create"
            editPath="/dashboard/compliance/affiliations/edit"
        />

    );

};

export default AffiliationsListPage;