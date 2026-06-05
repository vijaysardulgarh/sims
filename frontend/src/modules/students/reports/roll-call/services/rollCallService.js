import api from '../../../../../services/api/axios';

export const getRollCallFilters = () =>
    api.get(
        '/students/reports/roll-call/filters/'
    );

export const getRollCallReport = (
    params
) =>
    api.get(
        '/students/reports/roll-call/',
        {
            params,
        }
    );