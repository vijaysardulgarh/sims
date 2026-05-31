import api from '../../../../services/api/axios';

const endpoint = '/infrastructure/rooms/';

export const getRooms = () =>
    api.get(endpoint);

export const getRoom = (id) =>
    api.get(`${endpoint}${id}/`);

export const createRoom = (data) =>
    api.post(endpoint, data);

export const updateRoom = (id, data) =>
    api.put(`${endpoint}${id}/`, data);

export const deleteRoom = (id) =>
    api.delete(`${endpoint}${id}/`);