import api from '../../../../services/api/axios';

const endpoint =
    '/infrastructure/facilities/';

export const getFacilities = () =>
    api.get(endpoint);

export const getFacility = (id) =>
    api.get(`${endpoint}${id}/`);

export const createFacility = (
    data
) =>
    api.post(endpoint, data);

export const updateFacility = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteFacility = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );