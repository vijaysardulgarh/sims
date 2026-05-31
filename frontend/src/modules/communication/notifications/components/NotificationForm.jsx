import {
    useEffect,
    useState,
} from 'react';

import api from '../../../../services/api/axios';

const NotificationForm = ({
    formData,
    setFormData,
}) => {

    const [
        templates,
        setTemplates
    ] = useState([]);

    useEffect(() => {

        loadTemplates();

    }, []);

    const loadTemplates = async () => {

        try {

            const response =
                await api.get(
                    '/communications/communication-templates/'
                );

            setTemplates(
                response.data.results ||
                response.data
            );

        } catch (error) {

            console.error(error);
        }
    };

    return (
        <>
            <div className="mb-3">

                <label>
                    Template
                </label>

                <select
                    className="form-control"
                    value={
                        formData.template || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            template:
                                e.target.value,
                        })
                    }
                >
                    <option value="">
                        Select Template
                    </option>

                    {templates.map(
                        (template) => (

                            <option
                                key={template.id}
                                value={template.id}
                            >
                                {template.name}
                            </option>

                        )
                    )}

                </select>

            </div>

            <div className="mb-3">

                <label>
                    Subject
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.subject || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            subject:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Message
                </label>

                <textarea
                    rows="8"
                    className="form-control"
                    value={
                        formData.message || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            message:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Notification Type
                </label>

                <select
                    className="form-control"
                    value={
                        formData.notification_type || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            notification_type:
                                e.target.value,
                        })
                    }
                >
                    <option value="">
                        Select Type
                    </option>

                    <option value="EMAIL">
                        Email
                    </option>

                    <option value="SMS">
                        SMS
                    </option>

                    <option value="APP">
                        App Notification
                    </option>

                    <option value="WHATSAPP">
                        WhatsApp
                    </option>

                </select>

            </div>

            <div className="mb-3">

                <label>
                    Scheduled At
                </label>

                <input
                    type="datetime-local"
                    className="form-control"
                    value={
                        formData.scheduled_at || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            scheduled_at:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="form-check">

                <input
                    type="checkbox"
                    className="form-check-input"
                    checked={
                        formData.is_active ??
                        true
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            is_active:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Active
                </label>

            </div>

        </>
    );
};

export default NotificationForm;