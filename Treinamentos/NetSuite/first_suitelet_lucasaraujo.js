/**
.*@NApiVersion 2.x
.*@NScriptType Suitelet
.*/

define(['N/ui/serverWidget'], function(serverWidget){

    function onRequest(context) {
        if(context.request.method === 'GET') {
            var form = serverWidget.createForm({
                title: 'Formulário do Lucas Araújo'
            });

            form.addField({
                id: 'textfield',
                type: serverWidget.FieldType.TEXT,
                label: 'Campo de teste'
            });

            form.addSubmitButton({
                label: 'Enviar'
            });

            context.response.writePage(form);
        }
    }

    return {
        onRequest: onRequest
    }

});
