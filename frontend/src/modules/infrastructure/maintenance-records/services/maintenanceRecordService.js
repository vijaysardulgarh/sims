import api from '../../../../services/api/axios';

const endpoint =
    '/infrastructure/maintenance-records/';

export const getMaintenanceRecords = () =>
    api.get(endpoint);

export const getMaintenanceRecord = (id) =>
    api.get(`${endpoint}${id}/`);

export const createMaintenanceRecord = (
    data
) =>
    api.post(endpoint, data);

export const updateMaintenanceRecord = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteMaintenanceRecord = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );