import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

const RecognitionListPage = () => {

    const columns = [

        {
            key: 'recognition_type',
            label: 'Type',
        },

        {
            key: 'recognition_number',
            label: 'Recognition No.',
        },

        {
            key: 'issuing_authority',
            label: 'Authority',
        },

        {
            key: 'status',
            label: 'Status',
        },

    ];

    return (

        <CrudListPage
            title="Recognitions"
            endpoint="/compliance/recognitions/"
            columns={columns}
            addPath="/dashboard/compliance/recognitions/create"
            editPath="/dashboard/compliance/recognitions/edit"
        />

    );

};

export default RecognitionListPage;