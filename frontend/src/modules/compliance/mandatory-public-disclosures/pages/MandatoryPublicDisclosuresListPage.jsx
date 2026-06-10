import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

const MandatoryPublicDisclosuresListPage = () => {

    const columns = [

        {
            key: 'affiliation_number',
            label: 'Affiliation No.',
        },

        {
            key: 'school_code',
            label: 'School Code',
        },

        {
            key: 'principal_name',
            label: 'Principal',
        },

        {
            key: 'total_teachers',
            label: 'Teachers',
        },

        {
            key: 'student_teacher_ratio',
            label: 'Ratio',
        },

    ];

    return (

        <CrudListPage
            title="Mandatory Public Disclosures"
            endpoint="/compliance/mandatory-public-disclosures/"
            columns={columns}
            addPath="/dashboard/compliance/mandatory-public-disclosures/create"
            editPath="/dashboard/compliance/mandatory-public-disclosures/edit"
        />

    );

};

export default MandatoryPublicDisclosuresListPage;