/**
 * @NApiVersion 2.x
 * @NScriptType Portlet
 */

define(['N/ui/serverWidget'], function(serverWidget){
    function render(params){
        var meupt = params.portlet;
        meupt.titulo='Primeiro Portlet';
        var nomeCompleto = meupt.addField({
            id: 'text',
            type: serverWidget.FieldType.TEXT,
            label: 'Nome Completo'
        });
        
        var dataAniversario = meuptForm.addField({
            id: 'date',
            label: 'Data de Aniversário',
            type: serverWidget.FieldType.DATE
        });

        /*
         *  O código abaixo estiliza os itens em colunas.
         */
        nomeCompleto.updateBreakType({
            breakType: 'startcol'
        });

        meupt.setSubmitButton({
            url: 'http://www.netsuite.com',
            label: 'Carregar',
            target: '_top'
        });

    }

    return{
        render: render
    }
});
