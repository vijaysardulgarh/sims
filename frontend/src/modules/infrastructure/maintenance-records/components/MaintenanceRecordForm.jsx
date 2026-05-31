import {
    useEffect,
    useState,
} from 'react';

import api from '../../../../services/api/axios';

const MaintenanceRecordForm = ({
    formData,
    setFormData,
}) => {

    const [assets, setAssets] =
        useState([]);

    useEffect(() => {

        loadAssets();

    }, []);

    const loadAssets = async () => {

        try {

            const response =
                await api.get(
                    '/infrastructure/assets/'
                );

            setAssets(
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

                <label className="form-label">
                    Asset
                </label>

                <select
                    className="form-control"
                    value={
                        formData.asset || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            asset:
                                e.target.value,
                        })
                    }
                >
                    <option value="">
                        Select Asset
                    </option>

                    {assets.map((asset) => (

                        <option
                            key={asset.id}
                            value={asset.id}
                        >
                            {asset.asset_code}
                            {' - '}
                            {asset.name}
                        </option>

                    ))}
                </select>

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Maintenance Date
                </label>

                <input
                    type="date"
                    className="form-control"
                    value={
                        formData.maintenance_date ||
                        ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            maintenance_date:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Service Type
                </label>

                <select
                    className="form-control"
                    value={
                        formData.service_type ||
                        ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            service_type:
                                e.target.value,
                        })
                    }
                >
                    <option value="">
                        Select Type
                    </option>

                    <option value="PREVENTIVE">
                        Preventive
                    </option>

                    <option value="CORRECTIVE">
                        Corrective
                    </option>

                    <option value="REPAIR">
                        Repair
                    </option>

                    <option value="INSPECTION">
                        Inspection
                    </option>

                    <option value="OTHER">
                        Other
                    </option>

                </select>

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Vendor Name
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.vendor_name || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            vendor_name:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Cost
                </label>

                <input
                    type="number"
                    className="form-control"
                    value={
                        formData.cost || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            cost:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Next Due Date
                </label>

                <input
                    type="date"
                    className="form-control"
                    value={
                        formData.next_due_date || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            next_due_date:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Remarks
                </label>

                <textarea
                    rows="4"
                    className="form-control"
                    value={
                        formData.remarks || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            remarks:
                                e.target.value,
                        })
                    }
                />

            </div>
        </>
    );
};

export default MaintenanceRecordForm;