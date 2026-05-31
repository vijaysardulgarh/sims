import api from '../../../../services/api/axios';

const endpoint =
    '/communications/notifications/';

export const getNotifications = () =>
    api.get(endpoint);

export const getNotification = (id) =>
    api.get(`${endpoint}${id}/`);

export const createNotification = (
    data
) =>
    api.post(endpoint, data);

export const updateNotification = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteNotification = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );