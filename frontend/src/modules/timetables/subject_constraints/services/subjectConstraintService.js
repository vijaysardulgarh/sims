import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000'; 

const apiClient = axios.create({
    baseURL: API_BASE_URL,
});

apiClient.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access') || localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

export const SubjectConstraintService = {
    getClasses: () => apiClient.get('/api/academics/classes/'),
    getStreams: () => apiClient.get('/api/academics/streams/'),
    getSubjects: () => apiClient.get('/api/academics/subjects/'), // Added here to avoid import conflicts
    
    getRequirements: (classId, streamId) => {
        let url = `/api/timetables/subject-requirements/bulk_assign/?school_class=${classId}`;
        if (streamId) url += `&stream=${streamId}`;
        return apiClient.get(url);
    },

    getConstraints: (classId, streamId) => {
        let url = `/api/timetables/subject-constraints/bulk_assign/?school_class=${classId}`;
        if (streamId) url += `&stream=${streamId}`;
        return apiClient.get(url);
    },

    saveConstraints: (payload) => {
        return apiClient.post('/api/timetables/subject-constraints/bulk_assign/', payload);
    }
};