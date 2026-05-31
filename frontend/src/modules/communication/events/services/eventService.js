import api from '../../../../services/api/axios';

const endpoint =
    '/communications/events/';

export const getEvents = () =>
    api.get(endpoint);

export const getEvent = (id) =>
    api.get(`${endpoint}${id}/`);

export const createEvent = (
    data
) =>
    api.post(endpoint, data);

export const updateEvent = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteEvent = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );