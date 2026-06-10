import {
    useEffect,
    useState,
} from "react";

import api from "../../../../services/api/axios";

const NotificationForm = ({
    formData,
    setFormData,
}) => {

    const [
        templates,
        setTemplates,
    ] = useState([]);

    useEffect(() => {

        loadTemplates();

    }, []);

    const loadTemplates = async () => {

        try {

            const response =
                await api.get(
                    "/communications/communication-templates/"
                );

            setTemplates(
                response.data.results ||
                response.data
            );

        }

        catch (error) {

            console.error(error);

        }

    };

    const handleChange = (
        field,
        value
    ) => {

        setFormData({
            ...formData,
            [field]: value,
        });

    };

    return (

        <div className="space-y-6">

            <div
                className="
                    grid
                    grid-cols-1
                    md:grid-cols-2
                    gap-6
                "
            >

                {/* Template */}

                <div>

                    <label
                        className="
                            block
                            text-sm
                            font-medium
                            text-gray-700
                            mb-2
                        "
                    >
                        Template
                    </label>

                    <select
                        value={
                            formData.template || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "template",
                                e.target.value
                            )
                        }
                        className="
                            w-full
                            px-4
                            py-3
                            border
                            border-gray-300
                            rounded-xl
                            shadow-sm
                            focus:outline-none
                            focus:ring-2
                            focus:ring-blue-500
                        "
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

                {/* Notification Type */}

                <div>

                    <label
                        className="
                            block
                            text-sm
                            font-medium
                            text-gray-700
                            mb-2
                        "
                    >
                        Notification Type
                    </label>

                    <select
                        value={
                            formData.notification_type || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "notification_type",
                                e.target.value
                            )
                        }
                        className="
                            w-full
                            px-4
                            py-3
                            border
                            border-gray-300
                            rounded-xl
                            shadow-sm
                            focus:outline-none
                            focus:ring-2
                            focus:ring-blue-500
                        "
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

            </div>

            {/* Subject */}

            <div>

                <label
                    className="
                        block
                        text-sm
                        font-medium
                        text-gray-700
                        mb-2
                    "
                >
                    Subject
                </label>

                <input
                    type="text"
                    value={
                        formData.subject || ""
                    }
                    onChange={(e) =>
                        handleChange(
                            "subject",
                            e.target.value
                        )
                    }
                    className="
                        w-full
                        px-4
                        py-3
                        border
                        border-gray-300
                        rounded-xl
                        shadow-sm
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-500
                    "
                    placeholder="Enter notification subject"
                />

            </div>

            {/* Message */}

            <div>

                <label
                    className="
                        block
                        text-sm
                        font-medium
                        text-gray-700
                        mb-2
                    "
                >
                    Message
                </label>

                <textarea
                    rows={8}
                    value={
                        formData.message || ""
                    }
                    onChange={(e) =>
                        handleChange(
                            "message",
                            e.target.value
                        )
                    }
                    className="
                        w-full
                        px-4
                        py-3
                        border
                        border-gray-300
                        rounded-xl
                        shadow-sm
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-500
                    "
                    placeholder="Enter notification message"
                />

            </div>

            {/* Scheduled At */}

            <div>

                <label
                    className="
                        block
                        text-sm
                        font-medium
                        text-gray-700
                        mb-2
                    "
                >
                    Scheduled At
                </label>

                <input
                    type="datetime-local"
                    value={
                        formData.scheduled_at || ""
                    }
                    onChange={(e) =>
                        handleChange(
                            "scheduled_at",
                            e.target.value
                        )
                    }
                    className="
                        w-full
                        px-4
                        py-3
                        border
                        border-gray-300
                        rounded-xl
                        shadow-sm
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-500
                    "
                />

            </div>

        </div>

    );

};

export default NotificationForm;