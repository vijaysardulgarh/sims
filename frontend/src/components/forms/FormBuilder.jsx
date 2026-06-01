import Input from "../ui/Input";
import Select from "../ui/Select";
import Textarea from "../ui/Textarea";
import Switch from "../ui/Switch";

const FormBuilder = ({
    fields,
    values,
    onChange,
}) => {

    return (

        <div
            className="
                grid
                grid-cols-1
                md:grid-cols-2
                gap-4
            "
        >

            {fields.map((field) => {

                switch (field.type) {

                    case "text":

                        return (
                            <Input
                                key={field.name}
                                label={field.label}
                                name={field.name}
                                value={
                                    values[field.name] || ""
                                }
                                onChange={onChange}
                            />
                        );

                    case "number":

                        return (
                            <Input
                                key={field.name}
                                type="number"
                                label={field.label}
                                name={field.name}
                                value={
                                    values[field.name] || ""
                                }
                                onChange={onChange}
                            />
                        );

                    case "textarea":

                        return (
                            <div
                                key={field.name}
                                className="md:col-span-2"
                            >
                                <Textarea
                                    label={field.label}
                                    name={field.name}
                                    value={
                                        values[field.name] || ""
                                    }
                                    onChange={onChange}
                                />
                            </div>
                        );

                    case "select":

                        return (
                            <Select
                                key={field.name}
                                label={field.label}
                                name={field.name}
                                value={
                                    values[field.name] || ""
                                }
                                options={field.options}
                                onChange={onChange}
                            />
                        );

                    case "switch":

                        return (
                            <div
                                key={field.name}
                                className="space-y-2"
                            >
                                <label
                                    className="
                                        block
                                        text-sm
                                        font-medium
                                    "
                                >
                                    {field.label}
                                </label>

                                <Switch
                                    checked={
                                        values[field.name]
                                    }
                                    onChange={() =>
                                        onChange({
                                            target: {
                                                name: field.name,
                                                value:
                                                    !values[
                                                        field.name
                                                    ],
                                            },
                                        })
                                    }
                                />
                            </div>
                        );

                    default:
                        return null;
                }

            })}

        </div>

    );
};

export default FormBuilder;