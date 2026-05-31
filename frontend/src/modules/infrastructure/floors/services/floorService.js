import api from '../../../../services/api/axios';

const endpoint = '/infrastructure/floors/';

export const getFloors = () =>
    api.get(endpoint);

export const getFloor = (id) =>
    api.get(`${endpoint}${id}/`);

export const createFloor = (data) =>
    api.post(endpoint, data);

export const updateFloor = (id, data) =>
    api.put(`${endpoint}${id}/`, data);

export const deleteFloor = (id) =>
    api.delete(`${endpoint}${id}/`);